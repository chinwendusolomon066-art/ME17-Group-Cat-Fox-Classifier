import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Cat vs Fox Classifier", page_icon="🐾")

IMG_SIZE = (160, 160)
CLASS_NAMES = ["cats", "foxes"]

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("cat_fox_classifier.keras")
model = load_model()

st.title("🐾 Cat vs Fox Classifier")
st.write("Upload an image and the model will predict whether it's a cat or a fox.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_resized = image.resize(IMG_SIZE)
    img_array = np.array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]
    label = CLASS_NAMES[1] if prediction > 0.5 else CLASS_NAMES[0]
    confidence = prediction if prediction > 0.5 else 1 - prediction

    st.subheader(f"Prediction: {label.capitalize()}")
    st.write(f"Confidence: {confidence:.2%}")