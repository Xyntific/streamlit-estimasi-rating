import pickle
import streamlit as st

model = pickle.load(open('statistik_pemain.sav','rb'))

st.title('Estimasi Rating Player CSGO')

total_maps      = st.number_input('Input Total Map')
total_rounds    = st.number_input('input Total Rounds')
kd_diff         = st.number_input('Input Kill/Death Difference')
kd              = st.number_input('Input Kill/Death Ratio')


predict = ''


if st.button('Estimasi Rating Player'):
    predict = model.predict(
        [[total_maps,total_rounds,kd_diff,kd]]
    )
    st.write ('Estimasi Rating Pelayer :',predict)