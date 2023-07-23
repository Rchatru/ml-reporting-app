import streamlit as st


# Icon alojado en: https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4ca.png
# Ha sido necesario cambiar la ubicación del mismo ya que streamlit busca por defecto en maxcdn que ha sido cerrado
# https://github.com/twitter/twemoji/issues/580

st.set_page_config(
    page_title="ML Reporting",
    page_icon="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4ca.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/Rchatru/ml-reporting-app/',
        'Report a bug': "https://github.com/Rchatru/ml-reporting-app/issues",
        'About': "# ML Reporting Webapp. Roberto Chávez Trujillo."
    }
)

st.title('ML Reporting')

st.markdown("""In this app you can retrieve and compare the performance for different training runs, among varying ML
models, hyperparameters and features. Select in the left sidebar your desired combination to check the metrics and graphs.""")


with st.sidebar:
    st.write(Select your combination)
    dim = st.radio("Dimensionality red.", ("None", "PCA"))
    algo = st.radio("Choose Algorithm", ("SVM", "NB", "CART"))


    
