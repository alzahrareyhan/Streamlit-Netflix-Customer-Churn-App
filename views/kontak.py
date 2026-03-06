import streamlit as st

def show_kontak():
    st.markdown("# 📞 Kontak Saya")

    # =========================
    # Card utama kontak
    # =========================
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:16px; line-height:1.6;'>
    Jika Anda ingin menghubungi saya untuk pertanyaan atau kolaborasi, silakan melalui:
    </p>
    <ul>
      <li>📧 Email: <a href='mailto:alzahrareyhan@gmail.com' style='color:#e50914; font-weight:600;'>alzahrareyhan@gmail.com</a></li>
      <li>💼 LinkedIn: <a href='https://www.linkedin.com/in/reyhan-nandita-al-zahra-64a82a278/' target='_blank' style='color:#e50914; font-weight:600;'>Reyhan Nandita Al Zahra</a></li>
      <li>💻 GitHub: <a href='https://github.com/alzahrareyhan' target='_blank' style='color:#e50914; font-weight:600;'>alzahrareyhan</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # =========================
    # Optional: Form interaktif
    # =========================
    st.markdown("<h4>📩 Kirim Pesan</h4>", unsafe_allow_html=True)
    name = st.text_input("Nama")
    email = st.text_input("Email")
    message = st.text_area("Pesan")
    if st.button("Kirim Pesan"):
        st.success(f"Pesan dari {name} berhasil dikirim (simulasi)")

    st.markdown("</div>", unsafe_allow_html=True)