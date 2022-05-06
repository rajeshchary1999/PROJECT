import streamlit as st
import numpy as np
import pandas as pd
import time
import webbrowser

import pickle

classifier = pickle.load(open('classifier.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


def welcome():
    return "WELCOME ALL"


def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])

    print(prediction)
    return prediction


def main():
    st.title("Bank Note Authenticator")
    html_temp = """

    <div style="background-color:SlateBlue;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", " ")
    skewness = st.text_input("skewness", " ")
    curtosis = st.text_input("curtosis", " ")
    entropy = st.text_input("entropy", " ")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        if result == 1:
            with st.spinner('Wait for it...'):
                time.sleep(1)
        st.success('You have the Genuine Note'.format(result))
        st.balloons()

    if result == 0:
        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.error('You Have the Fake Note'.format(result))






if __name__ == '__main__':
    main()
