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

st.markdown(
    """
    # ☀️ SolSelex

    ### AI-Powered Solar Farm Site Selection & Land Suitability Analysis

    Upload a satellite image and receive an AI-powered engineering assessment
    for solar farm feasibility.
    """
)

st.markdown("---")

uploaded_file = st.file_uploader(
    "📤 Upload Satellite Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    left, right = st.columns([1, 1])

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name

    result = predict_image(temp_path)
    recommendation = get_recommendation(result["class"])

    with left:
        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

    with right:
        st.subheader("Prediction")

        st.metric("Land Type", result["class"])
        st.metric("Confidence", f"{result['confidence']*100:.2f}%")
        st.metric("Solar Suitability Score", recommendation["score"])

        st.success(recommendation["recommendation"])
        st.info(recommendation["reason"])

    st.divider()

    st.subheader("📊 Top Predictions")

    for pred in result["top_predictions"]:
        st.progress(pred["confidence"])
        st.write(
            f"**{pred['class']}** — {pred['confidence']*100:.2f}%"
        )

    os.remove(temp_path)