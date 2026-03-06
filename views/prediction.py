import streamlit as st
import pandas as pd
from utils.load_assets import load_model, load_encoders, load_scalers
from utils.preprocess import safe_encode, safe_scale

def show_prediction():
    # =======================
    # Load model, encoders, scalers
    # =======================
    model_data = load_model()
    model = model_data["model"]
    encoders = load_encoders()
    scalers = load_scalers()
    feature_names = model_data["feature_name"]

    # Apply CSS
    st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)

    # =======================
    # Header
    # =======================
    st.markdown("# 🔮 Prediction")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin-bottom:0.2rem;'>📺 Netflix Customer Churn Prediction</h1>", unsafe_allow_html=True)
    st.write("Fill in the customer data manually or upload an Excel/CSV file, then click **Predict** to see the churn probability.")
    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
    st.caption("Tip: Use *Auto-calculate derived features* to maintain consistency.")
    st.markdown("</div>", unsafe_allow_html=True)

    # =======================
    # Input method
    # =======================
    # st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📝 Input Method")
    input_method = st.radio("Choose input method:", ["Manual Input", "Upload File"])
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    input_df = None

    # =======================
    # Upload section dengan CSV guide
    # =======================
    if input_method == "Upload File":
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        
        with st.expander("📋 View Required CSV Format"):
            st.markdown("""
    Your CSV file should contain these columns:

    - age, gender, subscription_type, region, payment_method
    - number_of_profiles, device, favorite_genre
    - watch_hours, avg_watch_time_per_day, last_login_days, monthly_fee
    - watch_hours_per_profile, login_recent
            """)

            # Contoh 2 baris data
            example_data = pd.DataFrame([
                {"age":25, "gender":"Female","subscription_type":"Premium","region":"Asia",
                "payment_method":"Credit Card","number_of_profiles":2,"device":"Mobile",
                "favorite_genre":"Drama","watch_hours":20,"avg_watch_time_per_day":2,
                "last_login_days":3,"monthly_fee":15.99,"watch_hours_per_profile":10,"login_recent":1},
                {"age":35,"gender":"Male","subscription_type":"Standard","region":"Europe",
                "payment_method":"Debit Card","number_of_profiles":3,"device":"Laptop",
                "favorite_genre":"Comedy","watch_hours":15,"avg_watch_time_per_day":1.5,
                "last_login_days":10,"monthly_fee":12.99,"watch_hours_per_profile":5,"login_recent":0}
            ])
            st.dataframe(example_data)

        st.markdown("### 📂 Upload Customer Data (CSV / Excel)")
        uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])
        if uploaded_file:
            try:
                if uploaded_file.name.endswith(".csv"):
                    input_df = pd.read_csv(uploaded_file)
                else:
                    input_df = pd.read_excel(uploaded_file)
                st.success("File berhasil diunggah!")
                st.markdown("#### Preview Input Data")
                st.dataframe(input_df.head())
            except Exception as e:
                st.error(f"Error reading file: {e}")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
    # =======================
    # Manual input section
    # =======================
    if input_method == "Manual Input":
        colA, colB = st.columns([1,1])

        with colA:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 👤 Customer Profile")
            age = st.slider("Age", min_value=1, max_value=100, value=30, help="Customer's age in years")
            gender = st.selectbox("Gender", ["Female", "Male", "Other"], help="Customer gender")
            subscription_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"], help="Subscription tier")
            region = st.selectbox("Region", ["Africa","Asia","Europe","North America","Oceania","South America"], help="Customer's region")
            payment_method = st.selectbox("Payment Method", ["Credit Card","Crypto","Debit Card","Gift Card","PayPal"], help="Payment method used")
            number_of_profiles = st.number_input("Number of Profiles", min_value=1, max_value=5, value=2, help="Number of profiles under this account")
            st.markdown("</div>", unsafe_allow_html=True)

        with colB:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 📈 Usage Behavior")
            device = st.selectbox("Device", ["Desktop","Laptop","Mobile","TV","Tablet"], help="Device most used by the customer")
            favorite_genre = st.selectbox("Favorite Genre", ["Action","Comedy","Documentary","Drama","Horror","Romance","Sci-Fi"], help="Customer's favorite genre")
            watch_hours = st.slider("Watch Hours", min_value=0.0, max_value=50.0, value=5.0, help="Total number of hours watched per month")
            # Avg Watch Time Per Day → slider
            avg_watch_time_per_day = st.slider("Avg Watch Time Per Day", min_value=0.0, max_value=5.0, value=0.45, help="Average number of hours watched per day")
            last_login_days = st.slider("Last Login (days)", min_value=0, max_value=30, value=10, help="Number of days since last login")
            monthly_fee = st.number_input("Monthly Fee", min_value=0.0, value=13.99, help="Monthly subscription fee in USD")
            st.markdown("</div>", unsafe_allow_html=True)

        # Derived features
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🧩 Derived Features")
        auto_watch_hours_per_profile = watch_hours / number_of_profiles if number_of_profiles else 0.0
        auto_login_recent = 1 if last_login_days <=7 else 0
        use_auto = st.checkbox("Auto-calculate derived features (recommended)", value=True, help="Automatically calculate derived features for consistency")
        d1, d2 = st.columns([1,1])
        if use_auto:
            watch_hours_per_profile = auto_watch_hours_per_profile
            login_recent = auto_login_recent
            with d1: st.metric("Watch Hours / Profile", f"{watch_hours_per_profile:.2f}")
            with d2: st.metric("Login Recent", f"{login_recent} (<=7 days)")
        else:
            with d1: watch_hours_per_profile = st.number_input("Watch Hours / Profile", min_value=0.0, value=float(auto_watch_hours_per_profile), help="Watch hours divided per profile")
            with d2: login_recent = st.selectbox("Login Recent (0=No,1=Yes)", [0,1], index=int(auto_login_recent), help="Whether the customer logged in in last 7 days")
        st.markdown("</div>", unsafe_allow_html=True)

        input_data = {
            'age': age,'gender': gender,'subscription_type': subscription_type,
            'watch_hours': watch_hours,'last_login_days': last_login_days,
            'region': region,'device': device,'monthly_fee': monthly_fee,
            'payment_method': payment_method,'number_of_profiles': number_of_profiles,
            'avg_watch_time_per_day': avg_watch_time_per_day,'favorite_genre': favorite_genre,
            'watch_hours_per_profile': watch_hours_per_profile,'login_recent': login_recent
        }
        input_df = pd.DataFrame([input_data])

    # =======================
    # Prediction section
    # =======================
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns([1.2,1,1])
    with p1: predict_btn = st.button("Predict", use_container_width=True)
    with p2:
        st.markdown("### 🧾 Summary")
        if input_method=="Manual Input":
            st.write(f"Plan: **{subscription_type}** · Device: **{device}**")
            st.write(f"Region: **{region}** · Payment: **{payment_method}**")
        else:
            st.write("Upload file → summary tidak ditampilkan, hanya tabel hasil prediksi.")
    with p3:
        st.markdown("### ⚙️ Quick Checks")
        if input_method=="Manual Input":
            st.write(f"Profiles: **{number_of_profiles}**")
            st.write(f"Last login: **{last_login_days} days**")
        else:
            st.write(f"Rows: **{len(input_df) if input_df is not None else 0}**")
    st.markdown("</div>", unsafe_allow_html=True)

    # =======================
    # Run prediction
    # =======================
    if predict_btn:
        if input_df is None or input_df.empty:
            st.error("No input data provided!")
            return
        try:
            df_proc = safe_encode(input_df.copy(), encoders)
            df_proc = safe_scale(df_proc, scalers)
            df_proc = df_proc[feature_names]
            proba_list = model.predict_proba(df_proc)[:,1]
            pred_list = model.predict(df_proc)

            if input_method=="Manual Input":
                proba = proba_list[0]
                pred = pred_list[0]
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                r1,r2,r3 = st.columns([1,1,1])
                with r1: st.metric("Churn Probability", f"{proba:.2f}")
                with r2: st.metric("Prediction", "CHURN ❌" if int(pred)==1 else "STAY ✅")
                with r3:
                    st.write("Risk Meter")
                    color = "red" if int(pred)==1 else "green"
                    width_percent = proba*100 if int(pred)==1 else (1-proba)*100
                    st.markdown(f"""
                        <div style="background:{color}; width:{width_percent}%; height:25px; border-radius:12px; position:relative;">
                            <span style="position:absolute; left:50%; top:2px; transform:translateX(-50%);
                            font-weight:bold; color:white;">{width_percent:.2f}%</span>
                        </div>
                    """, unsafe_allow_html=True)
                if int(pred)==1:
                    st.error(f"Customer will Churn ❌ (Probability: {proba:.2f})")
                else:
                    st.success(f"Customer will Stay ✅ (Probability: {proba:.2f})")
                with st.expander("🔍 View processed model input (after encoding/scaling)"):
                    st.dataframe(df_proc)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                result_df = input_df.copy()
                result_df["Prediction"] = ["CHURN ❌" if p==1 else "STAY ✅" for p in pred_list]
                result_df["Probability"] = proba_list
                st.markdown("### 🔍 Hasil Prediksi")
                st.dataframe(result_df)
                csv_bytes = result_df.to_csv(index=False).encode()
                st.download_button(
                    label="Download Results as CSV",
                    data=csv_bytes,
                    file_name="prediksi_churn.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Prediction pipeline error: {e}")