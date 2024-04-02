import streamlit as st
#Judul aplikasi
st.title('Cholesterol Calculator For Foods🥩')  
        
#Intro Aplikasi
st.markdown('''Cholesterol Calculator For Foods digunakan untuk menghitung kalori pada bahan pangan hewani. Silahkan pilih Bahan pangan yang diinginkan......
            ☆*: .｡. o(≧▽≦)o .｡.:*☆''')

st.markdown('---')

from streamlit_option_menu import option_menu
#navigasi sidebar
with st.sidebar :
    selected = option_menu ('Kategori Bahan Pangan',
    ['Main Menu',
     'Susu dan Telur',
     'Ikan',
     'Daging',
     'Unggas'],
     default_index=0)
    
if (selected == 'Main Menu') :
    st.markdown('''KELOMPOK 7 (1E-PMIP):
            
    1. Kalisa Khatelya (2320532)
    2. Nayla Shafa Aulia (2320541)
    3. Selvi Wardayanti (2320555)
    4. Syifa Aprilya (2320558)
    5. Zikri (2320560)''') 

    st.header('💡:red[Tahukah] :blue[Anda]??')
    st.text('''
            Bahwa sama sekali tidak ada kolesterol dalam makanan nabati apa pun, 
            termasuk sereal, buah-buahan, sayuran, dan biji-bijian? 
            Kolesterol hanya berasal dari makanan hewani🐓🐄🐟''')
    
    st.text(''' 
                Bahan makanan hewani adalah sumber makanan yang dihasilkan dari hewan yang dapat
                dikonsumsi oleh manusia. Bahan pangan hewani dikenal sebagai sumber protein dan 
                lemak. Kandungan kolesterol dalam makanan sangat penting untuk diperhatikan, 
                seperti LDL (low-density lipoprotein, sering disebut sebagai kolesterol "jahat". 
                Sangat penting untuk memantau dan mengelola kadar LDL untuk menjaga kesehatan 
                jantung yang baik. Kalkulator kolesterol adalah alat yang dapat membantu Anda 
                mengetahui berapa banyak kolesterol dalam makanan yang Anda makan. Dengan kalkulator 
                kolesterol ini, Anda dapat dengan cepat menentukan asupan kolesterol harian dan 
                melacaknya. Seseorang yang berisiko terkena penyakit jantung harus menjaga konsumsi
                kolesterol hariannya sekitar 200 mg. Kalkulator ini juga akan memberikan Anda 
                informasi menarik tentang kandungan kolesterol dalam berbagai makanan.''')

if (selected == 'Susu dan Telur') :
    st.header('Jumlah Kolestrol Dalam Jenis Bahan Pangan Susu dan Telur', divider='blue')
    option = st.selectbox(
    'Pilih Jenis Makanan',
    ('Mentega', 'Keju', 'Susu','Yogurt', 'Kuning Telur', 'Telur Utuh'))
    Bobot_Makanan = st.number_input("Masukkan Bobot Makanan (gram)")

if (selected == 'Ikan') :
    st.header('Jumlah Kolestrol Dalam Jenis Bahan Pangan Ikan', divider='red')
    option = st.selectbox(
    'Pilih Jenis Makanan',
    ('ikan tuna', 'ikan salmon', 'ikan lele', 'ikan mujair', 'udang', 'ikan patin', 'ikan tongkol', 'ikan mas', 'ikan gurame', 'cumi-cumi'))
    Bobot_Makanan = st.number_input("Masukkan Bobot Makanan (gram)")

if (selected == 'Daging') :
    st.header('Jumlah Kolestrol Dalam Jenis Bahan Pangan Daging', divider='orange')
    option = st.selectbox(
    'Pilih Jenis Makanan',
    ('Daging sapi', 'Daging kambing', 'Daging kerbau', 'Daging Domba', 'Daging Unta'))
    Bobot_Makanan = st.number_input("Masukkan Bobot Makanan (gram)")

if (selected == 'Unggas') :
    st.header('Jumlah Kolestrol Dalam Jenis Bahan Pangan Unggas',divider='green')
    option = st.selectbox(
    'Pilih Jenis Makanan',
    ('Daging ayam', 'Daging bebek', 'Daging burung', 'Daging kalkun'))
    Bobot_Makanan = st.number_input("Masukkan Bobot Makanan (gram)")






