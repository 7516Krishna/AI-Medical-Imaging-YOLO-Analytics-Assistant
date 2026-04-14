import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from src.visualization import plot_bar, plot_pie, plot_line
from src.chat_assistant import generate_chat_response

# Load YOLO model
model = YOLO("runs/detect/train/weights/best.pt")

st.title("🧠 AI Medical Image Analysis System")

# Upload image
uploaded_file = st.file_uploader("Upload Medical Image")

if uploaded_file:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, caption="Uploaded Image")

    # YOLO prediction
    results = model(image)

    result_img = results[0].plot()

    st.image(result_img, caption="Detection Result")

    # Simulated prediction
    prediction = "pneumonia"
    confidence = 0.85

    st.subheader("📊 Analysis")

    labels = ["Normal", "Pneumonia"]
    values = [10, 40]

    st.pyplot(plot_bar(labels, values))
    st.pyplot(plot_pie(labels, values))

    confidence_values = [0.6, 0.7, 0.8, confidence]
    st.pyplot(plot_line(confidence_values))

    st.subheader("💬 Chat with AI Assistant")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_input = st.text_input("Ask about your diagnosis")

    if user_input:
        response = generate_chat_response(user_input, prediction, confidence)

        st.session_state.chat.append(("User", user_input))
        st.session_state.chat.append(("AI", response))

    for role, msg in st.session_state.chat:
        st.write(f"**{role}:** {msg}")