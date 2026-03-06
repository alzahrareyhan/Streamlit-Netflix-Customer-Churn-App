import streamlit as st
import time

def show_tentang_saya():
    st.markdown("# 👤 Tentang Saya")

    st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #E50914;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2], vertical_alignment="top")

    with col1:
        st.image("image/Reyhan.jpeg")

    with col2:
        st.markdown("""
        <div class="card">
         <p style="text-align: justify;">
         "Saya adalah lulusan Sarjana Teknik Informatika dari Universitas Negeri Semarang (2025) dengan minat pada Data Analyst, Data Science, AI Engineer, ML Engineer. Memiliki pengalaman dalam mengembangkan model prediktif, visualisasi data, serta solusi berbasis kecerdasan buatan dan aplikasi web, dengan kemampuan mengolah data terstruktur maupun tidak terstruktur serta merancang algoritma yang efisien untuk menyelesaikan permasalahan kompleks. Saya memiliki kemampuan analisis, pemecahan masalah, dan kerja tim yang baik serta berkomitmen untuk terus belajar dan berkontribusi dalam pengembangan solusi teknologi inovatif."
         </p>
         <p>
         <b>Nama:</b> Reyhan Nandita Al Zahra<br>
         <b>Role:</b> Data Analyst / Data Scientist<br>
         <b>Fokus:</b> Customer Analytics, Machine Learning, Visualisasi Data<br>
         <b>Keahlian:</b> Analisis Data, ML/AI, Visualisasi, Web Application Development
         </p>
        </div>
        """, unsafe_allow_html=True)

        # Skill bars animasi
        skills = {
            "Data Analysis": 95,
            "Machine Learning": 90,
            "AI/Deep Learning": 85,
            "Visualization": 90,
            "Web Application Development": 80
        }
        st.markdown("<b>Keahlian Utama:</b>", unsafe_allow_html=True)
        for skill, percent in skills.items():
            st.markdown(f"<p>{skill}</p>", unsafe_allow_html=True)
            bar = st.progress(0)
            for i in range(percent + 1):
                bar.progress(i)
                time.sleep(0.005)

    st.markdown("</div>", unsafe_allow_html=True)