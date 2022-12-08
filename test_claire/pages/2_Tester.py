#===============================================================================

import streamlit as st
#from PIL import Image
from include import take_a_picture, picture_to_df, picture_to_target
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,FunctionTransformer
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.compose import ColumnTransformer, make_column_transformer, make_column_selector
import dill

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Testons l'acquisition photo !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

picture = None
picture = take_a_picture(key=6453)
if picture:
    button1 = st.button("Tester la photo", key=1)

    if button1:
        df = picture_to_df(picture)
        # st.write(type(df))
        if type(df) == type("toto"):
            st.write("Problème dans l'acquisition photo.")
        else:
            st.write(df)
            # st.write(df.shape)
            # ###### target = picture_to_target(picture)
            #st.write(type(target))
            #st.write(target)
            #result = target[0][0]
            #prob = target[1][0]

            #st.write(target[0])
            #st.write(type(target[0]))
            model = SVC(kernel= 'poly', gamma = 1, coef0 = 0, C = 0.01, probability=True)
            # X_train = (X_train - X_train.mean()) / X_train.std()
            # rounder = FunctionTransformer(lambda array: np.round(array, decimals=2))
            normalizer = FunctionTransformer(lambda x: (x - x.mean()) / x.std())
            scaling = make_column_transformer((MinMaxScaler(), make_column_selector(dtype_include=['float64'])))
            pipeline = make_pipeline(normalizer, scaling)
            pipeline
            with open('pipe.pkl', 'rb') as file:
                trained_model = dill.load(file)
            y_pred = trained_model.predict(df)
            prob_pierre = round((target[1][0][0])*100)
            prob_feuille = round((target[1][0][1])*100)
            prob_ciseaux = round((target[1][0][2])*100)
            st.write (f'probabilité de Pierre : {prob_pierre} %')
            st.write (f'probabilité de Feuille : {prob_feuille} %')
            st.write (f'probabilité de Ciseaux : {prob_ciseaux} %')

            #st.write(type(target))
            #st.write(target.shape)
            html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            html_gesture = chifoudict[target[0][0]]
            st.markdown(html_gesture, unsafe_allow_html=True)
