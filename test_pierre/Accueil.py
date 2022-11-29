#===============================================================================

import matplotlib.pyplot as plt
import streamlit as st
import mediapipe as mp
import pandas as pd
from PIL import Image
import numpy as np
import random
import os
import cv2
from PIL import Image

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

def take_a_picture():
    picture = st.camera_input(label="", disabled=False)
    return picture


def picture_to_df(picture):
    hand_list = []
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        # Read the image, flip it around y-axis for correct handedness output (see above)
        # image = cv2.flip(cv2.imread(picture), 1)
        img = Image.open(picture)
        img_array = np.array(img)
        # image = cv2.flip(img_array, 1)
        image = img_array
        # st.image(image)
        #-------------------------------------
        # Convert the BGR image to RGB before processing.
        # results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        results = hands.process(image)
        if not results.multi_hand_landmarks:
            return "No hand in this picture!"
        # annotated_image = image.copy()
        for hand_landmarks in results.multi_hand_landmarks:
            # print((hand_landmarks.landmark))
            fingers = {}
            for i, finger in enumerate(hand_landmarks.landmark, start=1):
                fingers[f'{i}x'] = (finger.x)
                fingers[f'{i}y'] = (finger.y)
            hand_list.append(fingers)
        paper_df = pd.DataFrame(hand_list)
        return paper_df


def picture_to_target(picture):
    return random.randint(0,2)


def main1():
    picture1 = take_a_picture()
    button1 = st.button("Convert")
    if button1:
        df1 = picture_to_df(picture1)
        st.write(df1)

def main2():
    picture2 = take_a_picture()
    button2 = st.button("Classify")
    chifoudict = {0: "pierre", 1: "feuille", 2: "ciseaux"}
    num_res = picture_to_target(picture2)
    str_res = chifoudict[num_res]
    if button2:
        st.write(f"Position de votre main : {str_res}")


def main3():
    #---------------------------------------------------------------------------
    image_path = IMAGE_PATH + "chifoumi.jpg"
    chifoumi_image = Image.open(image_path)
    #---------------------------------------------------------------------------
    col1, col2 = st.columns(2)
    #---------------------------------------------------------------------------
    #-- Colonne 1
    picture = col1.image(chifoumi_image, width=400)
    #---------------------------------------------------------------------------
    #-- Colonne 2
    picture = col2.camera_input(label=" ", disabled=False, key=2)

def main4():
    image_path = IMAGE_PATH + "chifoumi.jpg"
    chifoumi_image = Image.open(image_path)
    picture = st.image(chifoumi_image, width=600)
    #button_play = st.button("Jouer")

def main5():
    st.balloons()

main4()
