import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder

# =========================
# HELPER FUNCTIONS (encoding/scaling)
# =========================
def get_choices(col, encoders):
    enc = encoders.get(col)
    if isinstance(enc, LabelEncoder):
        return list(enc.classes_)
    if isinstance(enc, OrdinalEncoder):
        return list(enc.categories_[0])
    return None

def safe_encode(input_df, encoders):
    for col, encoder in encoders.items():
        if col not in input_df.columns:
            continue
        if isinstance(encoder, OrdinalEncoder):
            input_df[[col]] = encoder.transform(input_df[[col]])
        elif isinstance(encoder, LabelEncoder):
            input_df[col] = encoder.transform(input_df[col].astype(str))
    return input_df

def safe_scale(input_df, scalers):
    scaler = scalers.get("StandardScaler")
    if scaler is None:
        return input_df
    scaler_cols = list(getattr(scaler, "feature_names_in_", []))
    if scaler_cols:
        input_df[scaler_cols] = scaler.transform(input_df[scaler_cols])
    return input_df

# =========================
# HALAMAN-HALAMAN (Pages)
# =========================

def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

# Tentang Proyek
def about_project():
    st.markdown("# Tentang Proyek")
    st.write("""
        Aplikasi ini dibangun untuk memprediksi kemungkinan pelanggan churn menggunakan data dari platform streaming.
        Model yang digunakan dilatih dengan data historis pelanggan, dan menggunakan fitur seperti usia, jenis kelamin,
        tipe langganan, serta perilaku menonton untuk memprediksi kemungkinan churn pelanggan.
    """)

# Tentang Saya
def about_me():
    st.markdown("# Tentang Saya")
    st.write("""
        Halo, saya adalah seorang pengembang aplikasi yang bekerja dengan menggunakan Streamlit, Python, dan berbagai teknik machine learning untuk membantu
        perusahaan dalam memahami perilaku pelanggan. Saya sangat tertarik dengan aplikasi kecerdasan buatan dalam industri hiburan.
    """)

# Prediksi Churn
def churn_prediction(model, encoders, scalers, feature_names):
    st.markdown("# Prediksi Churn")
    st.write("Isi data customer, lalu klik **Predict** untuk melihat potensi churn.")

    # Input fields
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    gender = st.selectbox("Gender", get_choices("gender", encoders) or ["Female", "Male", "Other"])
    subscription_type = st.selectbox("Subscription Type", get_choices("subscription_type", encoders) or ["Basic", "Standard", "Premium"])
    region = st.selectbox("Region", get_choices("region", encoders) or ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"])
    payment_method = st.selectbox("Payment Method", get_choices("payment_method", encoders) or ["Credit Card", "Crypto", "Debit Card", "Gift Card", "PayPal"])
    number_of_profiles = st.number_input("Number of Profiles", min_value=1, max_value=5, value=2)
    watch_hours = st.number_input("Watch Hours", min_value=0.0, value=5.0)
    avg_watch_time_per_day = st.number_input("Avg Watch Time Per Day", min_value=0.0, value=1.0)
    last_login_days = st.number_input("Last Login (days)", min_value=0, value=10)
    monthly_fee = st.number_input("Monthly Fee", min_value=0.0, value=13.99)

    # Derived features
    auto_watch_hours_per_profile = watch_hours / number_of_profiles if number_of_profiles else 0.0
    auto_login_recent = 1 if last_login_days <= 7 else 0
    use_auto = st.checkbox("Auto-calculate derived features (recommended)", value=True)

    if use_auto:
        watch_hours_per_profile = auto_watch_hours_per_profile
        login_recent = auto_login_recent
    else:
        watch_hours_per_profile = st.number_input("Watch Hours Per Profile", min_value=0.0, value=auto_watch_hours_per_profile)
        login_recent = st.selectbox("Login Recent (0 = No, 1 = Yes)", [0, 1], index=int(auto_login_recent))

    # Prediction button
    if st.button("Predict"):
        input_data = {
            'age': age,
            'gender': gender,
            'subscription_type': subscription_type,
            'watch_hours': watch_hours,
            'last_login_days': last_login_days,
            'region': region,
            'device': "Desktop",  # Assuming 'device' for simplicity
            'monthly_fee': monthly_fee,
            'payment_method': payment_method,
            'number_of_profiles': number_of_profiles,
            'avg_watch_time_per_day': avg_watch_time_per_day,
            'favorite_genre': "Action",  # Assuming 'favorite_genre'
            'watch_hours_per_profile': watch_hours_per_profile,
            'login_recent': login_recent
        }

        input_df = pd.DataFrame([input_data])
        input_df = safe_encode(input_df, encoders)
        input_df = safe_scale(input_df, scalers)

        missing_feats = [c for c in feature_names if c not in input_df.columns]
        if missing_feats:
            st.error(f"Model expects missing features: {missing_feats}")
            return

        input_df = input_df[feature_names]

        proba = model.predict_proba(input_df)[0][1]
        pred = model.predict(input_df)[0]

        st.metric("Churn Probability", f"{proba:.2f}")
        st.write("Prediction: **Churn**" if pred == 1 else "Prediction: **Stay**")
        st.progress(proba)

# Kontak Saya
def contact_me():
    st.markdown("# Kontak Saya")
    st.write("""
        Jika Anda memiliki pertanyaan atau ingin menghubungi saya untuk kolaborasi, silakan kirim pesan ke email saya di:
        [email@example.com](mailto:email@example.com).
    """)