import streamlit as st
import tempfile
import os

from src.models.predict import predict_image
from src.engine.recommendation import get_recommendation

st.set_page_config(
    page_title="SolSelex",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ SolSelex")
st.subheader("AI-Powered Solar Farm Site Selection")

uploaded_file = st.file_uploader(
    "Upload a satellite image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image", width=350)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name

    result = predict_image(temp_path)

    recommendation = get_recommendation(result["class"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Land Type",
            result["class"]
        )

        st.metric(
            "Confidence",
            f"{result['confidence']*100:.2f}%"
        )

    with col2:

        st.metric(
            "Solar Suitability Score",
            recommendation["score"]
        )

        st.metric(
            "Recommendation",
            recommendation["recommendation"]
        )

    st.subheader("Top Predictions")

    for pred in result["top_predictions"]:

        st.progress(pred["confidence"])

        st.write(
            f"{pred['class']} — {pred['confidence']*100:.2f}%"
        )

    os.remove(temp_path)