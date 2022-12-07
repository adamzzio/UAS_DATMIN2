import streamlit as st
from PIL import Image

# SET PAGE
pageicon = Image.open("aset_web/LOGO_WAZEEK.png")
st.set_page_config(page_title="Wazeek Web App", page_icon=pageicon, layout="centered")

# SET TITLE AND LOGO IMAGE
intro_col_left, intro_col_mid, intro_col_right = st.columns([1.5,6,0.5])
intro_col_mid.image('aset_web/LOGO_WAZEEK.png')
st.markdown('<div style="text-align: justify; font-size:250%"> <b>Web App Analisis Sentimen Resesi Ekonomi 2023</b> </div>',
            unsafe_allow_html=True)

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Web App Analisis Sentimen Resesi Ekonomi 2023 adalah sebuah aplikasi web yang membantu menganalisis sentimen atau persepsi publik terhadap resesi ekonomi di tahun 2023. Aplikasi ini mengumpulkan data dari berbagai sumber dan menggunakan teknik analisis sentimen untuk menghasilkan laporan yang membantu para pengambil keputusan mengetahui bagaimana persepsi masyarakat tentang resesi ekonomi yang mungkin terjadi di masa mendatang. Dengan menggunakan aplikasi ini, para pengambil keputusan dapat membuat keputusan yang lebih informatif dan tepat waktu. </div>',
            unsafe_allow_html=True)

# ANGGOTA TIM
st.write('####')
st.write('## Anggota Tim :')

col1, col2, col3 = st.columns(3)
col4, _, col6 = st.columns([4,1,4])
col7, _, col9 = st.columns([4,1,4])

foto_adamz = Image.open('aset_foto/foto_adam.jpeg').resize((400,400))
foto_naura = Image.open('aset_foto/foto_naura.png').resize((400,400))
foto_tyurr = Image.open('aset_foto/foto_tyur.jpeg').resize((400,400))
foto_ratuu = Image.open('aset_foto/foto_ratu.jpeg').resize((300,300))
foto_lidya = Image.open('aset_foto/foto_lidya.jpeg').resize((300,300))

# For columns 1 : Introduce Naura
col1.write('### Annaura Nabilla Masduki')
col1.image(foto_naura, caption = "162012133021")

# For columns 2 : Introduce Adam
col2.write('### Adam Maurizio Winata')
col2.image(foto_adamz, caption = "162012133045")

# For columns 3 : Introduce Tyur
col3.write("### Tyur Muthia Wardha Viani")
col3.image(foto_tyurr, caption = "162012133008")

# For columns 4 : Introduce Ratu
col4.write("### Qothrotunnidha' Almaulidiyah")
col7.image(foto_ratuu, caption = "162012133093")

# For columns 5 : Introduce Lidya
col6.write('### Lidya Septi Andini')
col9.image(foto_lidya, caption = "162012133052")