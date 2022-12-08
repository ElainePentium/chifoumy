#import matplotlib.pyplot as plt
import streamlit as st
import mediapipe as mp
import pandas as pd
from PIL import Image
import numpy as np
#import random
#import os
#import cv2
from chifoumy.interface.utils import create_key
#from chifoumy.ml_logic.registry import load_pipeline
#from chifoumy.ml_logic.preprocessor import preprocess_features


def take_a_picture(key):
    """
    Take a picture with streamlit.camera_input.
    """
    picture = st.camera_input(label="", disabled=False, key=key)
    return picture

def picture_to_df(picture):
    """
    This function take a picture of an hand as argument (created with
    streamlit.camera_input) and return a DataFrame which contains
    the mediapipe data of this hand.
    """
    hand_list = []
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        img = Image.open(picture)
        img_array = np.array(img)
        # image = cv2.flip(img_array, 1)
        image = img_array
        results = hands.process(image)
        if not results.multi_hand_landmarks:
            return "No hand in this picture!"
        for hand_landmarks in results.multi_hand_landmarks:
            fingers = {}
            for i, finger in enumerate(hand_landmarks.landmark, start=1):
                fingers[f'{i}x'] = (finger.x)
                fingers[f'{i}y'] = (finger.y)
                fingers[f'{i}z'] = (finger.z)
            hand_list.append(fingers)
        return pd.DataFrame(hand_list)
