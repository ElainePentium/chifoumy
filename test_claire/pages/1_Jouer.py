#===============================================================================

import streamlit as st
from PIL import Image
from include import take_a_picture, picture_to_target

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Jouons contre la machine !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#jeu_en_cours = 1

#while jeu_en_cours:
#    picture = take_a_picture(key=6453)
#    button1 = st.button("Test", key=1)


def main3():
    #---------------------------------------------------------------------------
    image_path1 = IMAGE_PATH + "ai.png"
    chifoumi_image = Image.open(image_path1)
    image_path2 = IMAGE_PATH + "blank.jpg"
    blank_image = Image.open(image_path1)
    # picture = st.camera_input(label="", disabled=False, key=17645)

#===============================================================================

# main3()

#===============================================================================

placeholder = st.empty()
button1 = placeholder.button('Lancer le jeu')
if button1:
    k = 0
    user_count = 0
    machine_count = 0
    st.write(f"Score du joueur     : {user_count}")
    st.write(f"Score de la machine : {machine_count}")
    while k < 2:
        placeholder.empty()
        picture = placeholder.camera_input(label=" ", disabled=False, key=975)
        button2 = st.button('Jouer')
        if button2:
            result = picture_to_target(picture)
            st.write(f"result={result}")
