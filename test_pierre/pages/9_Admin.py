#===============================================================================

import random
import streamlit as st
from chifoumy.interface.detection import take_a_picture, picture_to_df
from chifoumy.ml_logic.registry import load_pipeline
from chifoumy.interface.utils import create_key

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

MAX_SCORE = 3

def scoring(machine_gesture, user_gesture):
    """
    0: pierre,
    1: feuille,
    2: ciseaux
    """
    if user_gesture==machine_gesture:
        return "null"
    elif user_gesture==0 and machine_gesture==2:
        return "user"
    elif user_gesture == 1 and machine_gesture == 0:
        return "user"
    elif user_gesture == 2 and machine_gesture == 1:
        return "user"
    else:
        return "machine"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Administration</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#-------------------------------------------------------------------------------

button = st.button("Réinitialiser les scores")

if button:
    file = open("scores.txt", "w")
    file.write("0,0")
    file.close()
    st.write("✅ Scores réinitialisés à zéro.")
