# Memanggil Module
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Memanggil data
data = pd.read_csv('bank-full.csv', sep=';')


def run():

    # Bagian atas
    st.title('Exploratory Data Analysis - Bank Customer Data 2020')
    st.write('---')
    st.image('https://managementweekly.org/wp-content/uploads/2021/04/header.jpg')

    # Deskripsi awal
    st.title('Deskripsi')
    st.write('### Laman ini menjelaskan data customer yang digunakan untuk melatih model yang dibuat.')
    st.markdown('Sumber data: click [here](https://www.kaggle.com/datasets/psvishnu/bank-direct-marketing) untuk mengunjungi website.')

    # Bagian A Isi dari sebagian data
    st.title('A. Isi dari sebagian data')
    st.dataframe(data.head(5))
    st.write('### Data memiliki jumlah baris sebanyak 45211 baris dan jumlah atribut sebanyak 17 atribut.')

    # Bagian B. Data Overview
    st.title('B. Data Overview:')
    st.write('### Data Dimensions:')
    st.write('* Jumlah Fitur: 17')
    st.write('* Jumlah Baris: 45,211')
    st.write('### Attribute Descriptions:')
    st.write('* **age**: Age of the customer (Numerical)')
    st.write('* **job**: Type of job of the customer (Categorical)')
    st.write('* **marital**: Marital status of the customer (Categorical)')
    st.write('* **education**: Highest level of education attained by the customer (Categorical)')
    st.write('* **default**: Indicates if the customer has previously failed to make a credit payment ("yes": Default occurred, "no": No default) (Categorical)')
    st.write('* **balance**: Average annual income received by the customer in Euros (Numerical)')
    st.write('* **housing**: Housing loan status of the customer (Categorical)')
    st.write('* **loan**: Personal loan status of the customer ("yes": Loan taken, "no": No loan) (Categorical)')
    st.write('* **contact**: Type of communication previously made with the customer (Categorical)')
    st.write('* **day**: Day of the month when the last marketing communication occurred (Numerical)')
    st.write('* **month**: Month of the last marketing communication (Categorical)')
    st.write('* **duration**: Duration of the last marketing communication in seconds (Numerical)')
    st.write('* **campaign**: Total number of communications made with the customer during the current marketing campaign (Numerical)')
    st.write('* **pdays**: Number of days since the customer was last contacted for a previous marketing campaign. A value of -1 indicates that the customer has never been contacted (Numerical)')
    st.write('* **previous**: Total number of communications made with the customer during the previous marketing campaigns (Numerical)')
    st.write('* **poutcome**: Outcome of the previous marketing campaign (Categorical)')
    st.write('* **y**: Indicates whether the customer subscribed to a term deposit ("yes" or "no") (Categorical)')

    # Bagian C. Proporsi data per kategori
    st.title('C. Proporsi data per kategori:')
    st.header('Bar Chart for Categorical Feature')
    kolom_kategorik = [i for i in data.columns if data[i].dtype == 'O']
    kolom_numerik = [i for i in data.columns if data[i].dtype != 'O']
    categorical_column = st.selectbox('Select the categorical column:', kolom_kategorik)
    if categorical_column:
        counts = data[categorical_column].value_counts()
        plt.figure(figsize=(25, 15))
        counts.plot(kind='bar', color='skyblue')
        plt.title(f'Bar Chart of {categorical_column}', fontsize=30)
        plt.xlabel(categorical_column, fontsize=25)
        plt.ylabel('Count', fontsize=25)
        plt.xticks(rotation=0, fontsize=20)
        plt.yticks(fontsize=20) 
        plt.tight_layout()
        st.pyplot(plt)

    # Bagian D Distribusi data numerik
    st.title('D. Distribusi data numerik :')
    st.header('Histogram for Numerical Feature')
    numerical_column = st.selectbox('Select the numerical column:', kolom_numerik)
    if numerical_column:
        plt.figure(figsize=(10, 5))
        plt.hist(data[numerical_column], bins=10, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {numerical_column}', fontsize=20)  
        plt.xlabel(numerical_column, fontsize=16)                   
        plt.ylabel('Frequency', fontsize=16)                         
        plt.xticks(fontsize=14)                                      
        plt.yticks(fontsize=14)                                      
        plt.grid(axis='y', alpha=0.75)                              
        plt.tight_layout()
        st.pyplot(plt)

    # Bagian E. Outliers dalam data
    st.title('E. Outliers dalam data :')
    st.header('Outliers in Numerical Features')
    kolom_numerik = [i for i in data.columns if data[i].dtype != 'O']
    selection_1 = st.selectbox('Select the numerical column:', kolom_numerik, key='selectbox_numerical_column')
    st.subheader(f'Box Plot for {selection_1}')
    plt.figure(figsize=(10, 5))
    plt.boxplot(data[selection_1], vert=False)
    plt.title(f'Box Plot of {selection_1}', fontsize=20)
    plt.xlabel(selection_1, fontsize=16)
    plt.grid(axis='x', alpha=0.75)
    plt.tight_layout()
    st.pyplot(plt)

    # Bagian F. Relasi fitur numerik terhadap fitur target
    st.title('F. Relasi fitur numerik terhadap fitur target :')
    categorical_feature = st.selectbox('Select the categorical feature:', kolom_kategorik)
    count_df = data.groupby([categorical_feature, 'y']).size().unstack(fill_value=0)
    count_df.plot(kind='bar', stacked=True, figsize=(20, 10))
    plt.title(f'Relationship between {categorical_feature} and Target Feature', fontsize=20)
    plt.xlabel(categorical_feature, fontsize=16)
    plt.ylabel('Count', fontsize=16)
    plt.xticks(rotation=0)
    plt.legend(title='Target', fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    st.pyplot(plt)

    # Bagian G. Relasi fitur kategorik terhadap fitur target
    st.title('G. Relasi fitur kategorik terhadap fitur target :')
    kolom_numerik_3 = [i for i in data.columns if data[i].dtype != 'O']
    numerical_column_3 = st.selectbox('Select the numerical column:', kolom_numerik_3, key='selectbox_numerical_column2')
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=data['y'], y=data[numerical_column_3])
    plt.title(f'Box Plot of {numerical_column_3} vs y', fontsize=20)
    plt.xlabel('y', fontsize=16)
    plt.ylabel(numerical_column_3, fontsize=16)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    st.pyplot(plt)


if __name__ == '__main__':
    run()