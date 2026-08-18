# Importing Dependencies
import pickle
import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Loading Tokenizer File

with open("New folder/tokenizer.pkl", "rb" ) as file:
    tokenizer = pickle.load(file)

# Loading Model file

model = tf.keras.models.load_model(
    "New folder/imbd-setiment-analysis-classifier.h5"
)


# Streamlit UI

st.set_page_conf(
    page_title = "IMBD Sentiment Analysis",
    page_icon  ="🎬",
    layout = "centered"
)


# Page Title

st.title("🎬 IMDB Movie Review Sentiment Analysis")

# Review Input 

review = st.text_area(
    "Enter your movie review",
    placeholder = "Example: This movie was Good"
)

# Predict Button

if st.button("Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a correct movie review")

    else:
        # Converting texts into sequence
        sequence = tokenizer.texts_to_sequences([review])

        # padding 
        padded_sequences = pad_sequences(
            sequence, maxlen=200, padding="post", truncating="post"
        )

    prediction = model.predict(padded_sequences, verbos=0)
    probability = float(prediction[0][0])

    # Result 
    if probability >= 0.5:
        st.success("Positive Review")
    else:
        st.error("Negative Review")
