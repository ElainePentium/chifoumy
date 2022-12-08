#===============================================================================

import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.image as mpimg
import numpy as np
#-------------------------------------------------------------------------------

from chifoumy.interface.detection import take_a_picture, picture_to_df
#from include import picture_to_df
#from chifoumy.interface.detection import picture_to_target
from chifoumy.interface.utils import create_key
from chifoumy.ml_logic.registry import load_pipeline

#===============================================================================

IMAGE_PATH = "data_images/pierre/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Alimentons le dataset « pierre » !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#-------------------------------------------------------------------------------
# NEW CODE

picture = None
picture = take_a_picture(key=6453)
#picture = take_a_picture()
if picture:
    button1 = st.button("Sauvegarder la photo", key=1)
    if button1:
        df = picture_to_df(picture)
        if type(df) == type("toto"):
            st.write("Problème dans l'acquisition photo.")
        else:
            st.write("✅ Acquisition photo OK")
            #st.write("Voici le DataFrame :")
            #st.write(type(df))
            #st.write(df)
            #----
            my_pipeline = load_pipeline()
            target = my_pipeline.predict(df)
            target = target[0]
            #st.write(f"target={target}")
            #----
            html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            texte_pierre = "Votre geste : pierre"
            texte_feuille = "Votre geste : feuille"
            texte_ciseaux = "Votre geste : ciseaux"
            simpledict = {0: texte_pierre, 1: texte_feuille, 2: texte_ciseaux}
            html_gesture = chifoudict[target]
            texte_gesture = simpledict[target]
            st.write(f"✅ {texte_gesture}")
            #st.markdown(html_gesture, unsafe_allow_html=True)
            #----
            file_name = IMAGE_PATH + "image_" + str(create_key()) + ".png"
            # file_name = "image_" + str(create_key()) + ".png"
#            # picture.save(file_name) ?
#            st.write(f"Écriture ddans le ficjier '{file_name}'")
#            with open(file_name, "wb") as f:
#                f.write(picture.getbuffer())
#                st.success("Saved File")
            img_pil = Image.open(picture)
            img_pil.save(file_name)
            st.write(f"✅ Sauvegarde de la photo '{file_name}'.")
