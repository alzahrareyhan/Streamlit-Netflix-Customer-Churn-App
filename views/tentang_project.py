# views/tentang_project.py
import streamlit as st

def show_tentang_project():
    st.markdown("# 📚 Tentang Proyek")  # Page title
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    # --------------------------

    # --------------------------
    st.markdown("""
    <h2>Alur Proyek & Deployment</h2>
    <div class="flow-container">
        <div class="flow-box">📊<br>Data Pelanggan<br><span>Profil & Perilaku Menonton</span></div>
        <div class="flow-arrow">➜</div>
        <div class="flow-box">⚙️<br>Preprocessing<br><span>Encoding & Scaling</span></div>
        <div class="flow-arrow">➜</div>
        <div class="flow-box">🤖<br>Model XGBoost<br><span>Prediksi Churn</span></div>
        <div class="flow-arrow">➜</div>
        <div class="flow-box">🏆<br>Output & Retensi<br><span>Status & Probabilitas</span></div>
    </div>

    <style>
        .flow-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 30px 0;
        }
        .flow-box {
            background-color: #e50914;
            color: white;
            padding: 25px 20px;
            border-radius: 12px;
            text-align: center;
            flex:1;
            font-weight: 600;
            box-shadow: 0 8px 15px rgba(0,0,0,0.3);
            transition: transform 0.2s;
        }
        .flow-box span {
            font-weight: normal;
            font-size: 14px;
        }
        .flow-box:hover {
            transform: translateY(-5px);
        }
        .flow-arrow {
            flex:0.05;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # --------------------------
    # Cards: Latar Belakang, Problem, Objective, etc.
    # --------------------------
    def render_card(title, content):
        st.markdown(f"""
        <div class="card">
            <h2>{title}</h2>
            {content}
        </div>
        """, unsafe_allow_html=True)

    # LATAR BELAKANG
    render_card("Latar Belakang",
        "<ul>"
        "<li>Churn pelanggan (~50%) berdampak pada pendapatan & pertumbuhan platform.</li>"
        "<li>Analisis data pelanggan untuk memahami faktor churn dan merancang strategi retensi.</li>"
        "<li>Fokus pada demografi, perilaku menonton, paket langganan, dan metode pembayaran.</li>"
        "</ul>"
    )

    # PROBLEM STATEMENT
    render_card("Problem Statement",
        "<ul>"
        "<li>Tingkat churn tinggi (~50%) → mengurangi recurring revenue.</li>"
        "<li>Perusahaan belum memahami faktor utama churn berbasis data.</li>"
        "<li>Strategi retensi kurang tepat tanpa identifikasi pola risiko churn.</li>"
        "</ul>"
    )

    # MAIN OBJECTIVE
    render_card("Main Objective",
        "<ul>"
        "<li>Menganalisis faktor-faktor yang memengaruhi churn pelanggan.</li>"
        "<li>Membangun model prediksi churn untuk tindakan preventif.</li>"
        "<li>Menghasilkan strategi berbasis data untuk menurunkan churn & meningkatkan retensi.</li>"
        "</ul>"
    )

    # SPECIFIC OBJECTIVES
    render_card("Specific Objectives",
        "<ul>"
        "<li>Identifikasi faktor penyebab churn: subscription, payment, perilaku menonton.</li>"
        "<li>Optimalkan pengalaman pelanggan agar bertahan lebih lama.</li>"
        "<li>Tingkatkan pendapatan berulang dari pelanggan yang tetap berlangganan.</li>"
        "</ul>"
    )

    # ANALISIS MODEL
    render_card("Analisis Model",
        "<ul>"
        "<li>Model: XGBoost Tuning, Accuracy: <span class='kpi'>99.6%</span></li>"
        "<li>Recall, Precision, F1-Score: tinggi → deteksi churn & non-churn akurat</li>"
        "<li>AUC ≈ 1 → model sangat baik membedakan kelas 0 & 1</li>"
        "<li>Fitur paling berpengaruh: <b>avg_watch_time_per_day, last_login_days, watch_hours, number_of_profiles</b></li>"
        "</ul>"
    )

    # IMPACT / BENEFIT
    render_card("Impact / Benefit",
        "<ul>"
        "<li>Prediksi churn real-time & interaktif melalui Streamlit.</li>"
        "<li>Membantu tim marketing/retensi mengambil tindakan preventif pada pelanggan berisiko tinggi.</li>"
        "<li>Menurunkan churn → meningkatkan retention & recurring revenue.</li>"
        "<li>Data-driven insights → strategi retensi lebih tepat sasaran.</li>"
        "</ul>"
    )

    # --------------------------
    # Global CSS for cards & KPI
    # --------------------------
    st.markdown("""
    <style>
        .card {
            background-color: #1d1d1d;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            color: #f5f5f5;
            box-shadow: 0 12px 20px rgba(0,0,0,0.3);
        }
        h2 {
            color: #e50914;
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 15px;
        }
        .kpi {
            font-size: 22px;
            color: #e50914;
            font-weight: bold;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        li {
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True)