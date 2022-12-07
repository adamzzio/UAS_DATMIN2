# IMPORT LIBRARY
import streamlit as st
from PIL import Image

# SET PAGE
pageicon = Image.open("aset_web/LOGO_WAZEEK.png")
st.set_page_config(page_title="Wazeek Web App", page_icon=pageicon, layout="centered")

# ---- SIDEBAR ----
st.sidebar.header("Articles")

jenis_berita = st.sidebar.selectbox(
    'Pilih berita di sini',
    ('Pengertian Resesi Ekonomi dan Faktor-Faktor yang Menyebabkannya',
     'Bagaimana Resesi Ekonomi Mempengaruhi Nilai Tukar Mata Uang dan Tingkat Suku Bunga',
     'Resesi Ekonomi dan Peran Penting Pemulihan Ekonomi setelah Terjadinya Resesi',
     'Bagaimana Resesi Ekonomi Mempengaruhi Konsumsi dan Investasi Masyarakat',
     'Resesi Ekonomi dan Implikasinya terhadap Pertumbuhan Ekonomi Jangka Panjang'))

# MENAMPILKAN BERITA
if jenis_berita == 'Pengertian Resesi Ekonomi dan Faktor-Faktor yang Menyebabkannya':
    st.header('Pengertian Resesi Ekonomi dan Faktor-Faktor yang Menyebabkannya')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi adalah masa penurunan aktivitas ekonomi yang terjadi dalam suatu negara. Biasanya ditandai dengan penurunan produksi, lapangan kerja, dan penjualan. Resesi ekonomi dapat terjadi karena berbagai faktor, di antaranya: </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Krisis keuangan global: Turunnya harga saham dan krisis utang dapat menyebabkan resesi ekonomi.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Penurunan permintaan: Jika permintaan terhadap produk atau jasa menurun, maka perusahaan akan mengurangi produksi, yang pada akhirnya dapat menyebabkan resesi ekonomi.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Inflasi yang tinggi: Inflasi yang tinggi dapat menyebabkan konsumen enggan untuk membelanjakan uang mereka, sehingga menurunkan permintaan. Hal ini dapat menyebabkan resesi ekonomi.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Perang dagang: Perang dagang dapat menyebabkan harga barang dan jasa meningkat, sehingga menurunkan permintaan dan menyebabkan resesi ekonomi.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Penurunan harga minyak: Penurunan harga minyak dapat menurunkan pendapatan negara yang bergantung pada ekspor minyak, sehingga dapat menyebabkan resesi ekonomi.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Untuk menghindari resesi ekonomi, pemerintah biasanya akan mengambil langkah-langkah seperti menurunkan suku bunga, meningkatkan belanja pemerintah, dan mengeluarkan stimulus fiskal. Namun, perlu diingat bahwa resesi ekonomi tidak dapat dihindari sepenuhnya dan dapat terjadi kapan saja. Oleh karena itu, penting bagi negara dan perusahaan untuk mempersiapkan diri dengan baik agar dapat menghadapi resesi ekonomi jika terjadi. </div>',
        unsafe_allow_html=True)
elif jenis_berita == 'Bagaimana Resesi Ekonomi Mempengaruhi Nilai Tukar Mata Uang dan Tingkat Suku Bunga':
    st.header('Bagaimana Resesi Ekonomi Mempengaruhi Nilai Tukar Mata Uang dan Tingkat Suku Bunga')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi dapat mempengaruhi nilai tukar mata uang dan tingkat suku bunga dalam beberapa cara. Pertama, ketika terjadi resesi ekonomi, permintaan terhadap produk dan jasa menurun. Hal ini dapat menyebabkan penurunan nilai mata uang negara tersebut, karena permintaan terhadap mata uang juga menurun. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kedua, resesi ekonomi dapat menyebabkan inflasi yang rendah. Inflasi yang rendah dapat menyebabkan bank sentral menurunkan suku bunga untuk mendorong pertumbuhan ekonomi. Hal ini dapat menyebabkan nilai tukar mata uang negara tersebut meningkat, karena suku bunga yang lebih rendah dapat menarik investor untuk membeli mata uang negara tersebut. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Ketiga, resesi ekonomi juga dapat menyebabkan investor mengalihkan investasi mereka ke mata uang negara lain yang lebih stabil. Hal ini dapat menyebabkan nilai tukar mata uang negara yang sedang mengalami resesi ekonomi menurun. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi dapat mempengaruhi nilai tukar mata uang dan tingkat suku bunga dalam beberapa cara. Oleh karena itu, penting bagi negara untuk mempersiapkan diri dengan baik untuk menghadapi resesi ekonomi dan meminimalkan dampaknya terhadap nilai tukar mata uang dan tingkat suku bunga. </div>',
        unsafe_allow_html=True)

elif jenis_berita == 'Resesi Ekonomi dan Peran Penting Pemulihan Ekonomi setelah Terjadinya Resesi':
    st.header('Resesi Ekonomi dan Peran Penting Pemulihan Ekonomi setelah Terjadinya Resesi')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi adalah masa penurunan aktivitas ekonomi yang terjadi dalam suatu negara. Resesi ekonomi dapat menyebabkan penurunan produksi, lapangan kerja, dan penjualan. Untuk mengatasi resesi ekonomi, pemerintah biasanya akan mengambil langkah-langkah seperti menurunkan suku bunga, meningkatkan belanja pemerintah, dan mengeluarkan stimulus fiskal. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Setelah resesi ekonomi teratasi, pemulihan ekonomi menjadi sangat penting untuk memulihkan pertumbuhan ekonomi yang sehat. Pemulihan ekonomi dapat dilakukan dengan cara-cara seperti meningkatkan investasi, meningkatkan ekspor, dan menciptakan lapangan kerja baru. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Pemerintah juga dapat mengambil langkah-langkah seperti menurunkan pajak, mengeluarkan stimulus fiskal, dan meningkatkan belanja pemerintah untuk mendukung pemulihan ekonomi. Hal ini dapat membantu meningkatkan permintaan, meningkatkan produksi, dan menciptakan lapangan kerja baru. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Peran penting pemulihan ekonomi setelah terjadinya resesi ekonomi tidak hanya terbatas pada negara yang mengalami resesi saja, tetapi juga dapat mempengaruhi perekonomian global. Dengan pemulihan ekonomi yang sehat, negara dapat kembali menjadi salah satu pelaku utama dalam perekonomian global dan meningkatkan stabilitas ekonomi secara keseluruhan. </div>',
        unsafe_allow_html=True)

elif jenis_berita == 'Bagaimana Resesi Ekonomi Mempengaruhi Konsumsi dan Investasi Masyarakat':
    st.header('Bagaimana Resesi Ekonomi Mempengaruhi Konsumsi dan Investasi Masyarakat')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi dapat mempengaruhi konsumsi dan investasi masyarakat dalam beberapa cara. Pertama, ketika terjadi resesi ekonomi, banyak orang yang kehilangan pekerjaan mereka atau mendapatkan gaji yang lebih rendah. Hal ini dapat menyebabkan konsumen enggan untuk membelanjakan uang mereka, sehingga menurunkan konsumsi. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kedua, resesi ekonomi juga dapat menyebabkan harga-harga barang dan jasa meningkat, sehingga mengurangi daya beli masyarakat. Hal ini dapat menyebabkan konsumen enggan untuk membelanjakan uang mereka, sehingga menurunkan konsumsi. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Ketiga, resesi ekonomi dapat menyebabkan investor enggan untuk menanamkan modal mereka karena takut akan potensi kerugian. Hal ini dapat menurunkan investasi, sehingga mengurangi pertumbuhan ekonomi. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi dapat mempengaruhi konsumsi dan investasi masyarakat dalam beberapa cara. Oleh karena itu, penting bagi pemerintah dan perusahaan untuk mempersiapkan diri dengan baik untuk menghadapi resesi ekonomi dan meminimalkan dampaknya terhadap konsumsi dan investasi masyarakat. </div>',
        unsafe_allow_html=True)

elif jenis_berita == 'Resesi Ekonomi dan Implikasinya terhadap Pertumbuhan Ekonomi Jangka Panjang':
    st.header('Resesi Ekonomi dan Implikasinya terhadap Pertumbuhan Ekonomi Jangka Panjang')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi adalah masa ketika pertumbuhan ekonomi mengalami penurunan secara signifikan, yang ditandai oleh turunnya produksi, lapangan kerja, dan pendapatan. Resesi juga dapat diidentifikasi dengan menurunnya aktivitas bisnis dan investasi, serta meningkatnya tingkat kegagalan bisnis dan peningkatan utang. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Resesi ekonomi dapat memiliki dampak yang sangat merugikan bagi pertumbuhan ekonomi jangka panjang. Hal ini dikarenakan resesi dapat menyebabkan penurunan investasi dan pengurangan lapangan kerja, yang pada gilirannya dapat menyebabkan penurunan pendapatan dan konsumsi. Penurunan konsumsi ini akan berdampak pada penurunan permintaan terhadap produk dan jasa, yang pada akhirnya dapat menyebabkan penurunan produksi. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Untuk mengatasi dampak negatif dari resesi ekonomi, pemerintah biasanya akan mengambil tindakan-tindakan fiskal dan moneter untuk menstimulasi pertumbuhan ekonomi. Tindakan fiskal meliputi pengurangan pajak dan peningkatan belanja pemerintah, sedangkan tindakan moneter meliputi penurunan suku bunga dan peningkatan jumlah uang yang beredar di masyarakat. Namun, ada kalanya tindakan-tindakan ini tidak cukup efektif dalam mengatasi resesi, terutama jika resesi tersebut disebabkan oleh faktor-faktor struktural dalam perekonomian. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Oleh karena itu, penting bagi pemerintah dan pelaku bisnis untuk mengambil langkah-langkah preventif untuk mengurangi kemungkinan terjadinya resesi ekonomi. Hal ini dapat dilakukan dengan cara menjaga stabilitas harga, menjaga agar pertumbuhan ekonomi tetap stabil, dan meningkatkan produktivitas dan inovasi di sektor-sektor penting dalam perekonomian. Dengan cara ini, pertumbuhan ekonomi jangka panjang dapat terjaga, dan resesi ekonomi dapat dicegah sebelum terjadi. </div>',
        unsafe_allow_html=True)