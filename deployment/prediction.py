import pandas as pd
import joblib
import streamlit as st


# Mengambil model yang disimpan
loaded_model = joblib.load('model.joblib')

def run():
    st.title('Customer Behavior Prediction')

    st.write('''Laman ini dapat digunakan untuk memprediksi apakah customer tertentu memiliki kemungkinan tinggi menerima tawaran Deposito Tetap''')

    with st.form(key='form_parameters'):
        age = st.number_input('Umur :', min_value=10, max_value = 100, step=1)
        job = st.selectbox('Pekerjaan :', ('management', 'technician', 'entrepreneur', 'blue-collar',
                                        'retired', 'admin.', 'services', 'self-employed',
                                        'unemployed', 'housemaid', 'student', 'unknown'))
        marital = st.selectbox('Kondisi Perkawinan :', ('married', 'single', 'divorced', 'unknown'))
        education = st.selectbox('Edukasi :', ('tertiary', 'secondary', 'primary', 'unknown'))
        default = st.selectbox('Default :', ('yes', 'no', 'unknown'))
        balance = st.number_input('Saldo :', min_value=-10000, max_value = 200000, step=1)
        housing = st.selectbox('Kepemilikan Rumah :', ('yes', 'no', 'unknown'))
        loan = st.selectbox('Memiliki Loan? :', ('yes', 'no', 'unknown'))
        contact = st.selectbox('Jenis Komunikasi :', ('cellular', 'telephone', 'unknown'))
        day = st.number_input('Hari Komunikasi :', 1, 31, 1)
        month = st.selectbox('Bulan Komunikasi :', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'unknown'))
        duration = st.number_input('Durasi Komunikasi :', 0, 10000, 10)
        campaign = st.number_input('Jumlah Campaign :', 1, 100, 10)
        pdays = st.number_input('Pdays :', -1, 100, 10)
        previous = st.number_input('Previous :', 0, 300, 10)
        poutcome = st.selectbox('Poutcome :', ('success', 'failure', 'other', 'unknown'))
        submit = st.form_submit_button('Predict')


    data = pd.DataFrame([{
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'default': default,
        'balance': balance,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'day': day,
        'month': month,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome
    }])

    data = data.replace('unknown', None)

    st.dataframe(data)


    if submit:
        pred = loaded_model.predict(data)
        st.write(pred)
        if str(pred[0]) == 'yes':
            st.write('Berdasarkan hasil prediksi, customer dengan karakteristik yang sudah diisi sebelumnya COCOK dilakukan penawaran.')
        else:
            st.write('Berdasarkan hasil prediksi, customer dengan karakteristik yang sudah diisi sebelumnya TIDAK COCOK dilakukan penawaran.')
            
if __name__ == '__main__':
    run()