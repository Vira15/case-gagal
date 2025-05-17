import streamlit as st

st.title('Perkalian')

panjang = st.number_input ("Masukkan nilai panjang", 0)
lebar = st.number_input ("Masukkan nilai lebar", 0)
hitung = st.button ("Hasil =")

if hitung :
    luas = panjang * lebar
    st.write ("Hasil = ", luas)
    st.success ("Hasil = {luas}")