#===============================================================================

import streamlit as st
#from PIL import Image
import pandas as pd
from chifoumy.interface.detection import take_a_picture, picture_to_df
#from chifoumy.interface.detection import picture_to_target
#from chifoumy.interface.utils import create_key
from chifoumy.ml_logic.registry import load_pipeline

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Testons l'acquisition photo !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

picture = None
picture = take_a_picture(key=666)
if picture:
    button1 = st.button("Tester la photo", key=1234)
    if button1:
        df = picture_to_df(picture)
        # st.write(type(df))
        if type(df) == type("toto"):
            st.write("Problème dans l'acquisition photo.")
        else:
            #st.write(df)
            my_pipeline = load_pipeline()
            target = my_pipeline.predict(df)
            target = target[0]
            #st.write(type(target))
            #st.write(target.shape)
            html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            html_gesture = chifoudict[target]
            st.markdown(html_gesture, unsafe_allow_html=True)
