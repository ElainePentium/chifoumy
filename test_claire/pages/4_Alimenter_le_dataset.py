#===============================================================================

import streamlit as st
from PIL import Image
from include import take_a_picture, picture_to_df, picture_to_target
from include import create_key
import pandas as pd
import matplotlib.image as mpimg
import numpy as np
import mediapipe as mp

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Alimentons le dataset !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#-------------------------------------------------------------------------------
# NEW CODE

picture = None
picture = take_a_picture(key=6453)
if picture:
    button1 = st.button("Sauvegarder la photo", key=1)
    if button1:
        df = picture_to_df(picture)
        if type(df) == type("toto"):
            st.write("Problème dans l'acquisition photo.")
        else:
            st.write("Voici le DataFrame :")
            st.write(type(df))
            st.write(df)
            file_name = "data_images/image_" + str(create_key()) + ".png"
            # file_name = "image_" + str(create_key()) + ".png"
            st.write(f"Sauvegarde de la photo '{file_name}'...")
#            # picture.save(file_name) ?
#            st.write(f"Écriture ddans le ficjier '{file_name}'")
#            with open(file_name, "wb") as f:
#                f.write(picture.getbuffer())
#                st.success("Saved File")
            img_pil = Image.open(picture)
            img_pil.save(file_name)
            st.write("... sauvegarde terminée.")
            #img_array = np.array(img_pil)
            #mpimg.imsave(file_name, img_array)
            #target = picture_to_target(picture)
            #target = target[0]
            #st.write(type(target))
            #st.write(target.shape)
            #html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            #html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            #html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            #chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            #html_gesture = chifoudict[target]
            #st.markdown(html_gesture, unsafe_allow_html=True)





#picture_alim = None
#picture_alim = take_a_picture(key=create_key())
#if picture_alim:
#    button_alim = st.button("Sauvegarder la photo", key=create_key())
#    if button_alim:
#        st.write("Clic")
#        df = picture_to_df(picture)
#        st.write(type(df))
#        if type(df) == type("toto"):
#            st.write("Problème dans l'acquisition photo.")
#        else:
#            st.write("Voici le DataFrame :")
#            st.write(df)
#            file_name = "image_" + create_key() + ".jpg"
#            # picture.save(file_name) ?
#            st.write(f"Écriture ddans le ficjier '{file_name}'")
#            with open(file_name, "wb") as f:
#                f.write(picture.getbuffer())
#                st.success("Saved File")




            #target = picture_to_target(picture)
            #target = target[0]
            #st.write(type(target))
            #st.write(target.shape)
            #html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            #html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            #html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            #chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            #html_gesture = chifoudict[target]
            #st.markdown(html_gesture, unsafe_allow_html=True)

#-------------------------------------------------------------------------------
# OLD CODE

#if picture:
#    button_save = st.button("Sauvegarder", key = create_key())
#    if button_save:
#        df = picture_to_df(picture)
#        if type(df) == type("toto"):
#            st.write("Problème dans l'acquisition photo.")
#        else:
#            file_name = "image_" + create_key() + ".jpg"
#            # picture.save(file_name) ?
#            with open(file_name, "wb") as f:
#                f.write(picture.getbuffer())
#                st.success("Saved File")
