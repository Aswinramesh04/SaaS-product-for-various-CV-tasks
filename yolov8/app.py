from pathlib import Path

import streamlit as st

import settings
import helper

# Setting page layout🤖
st.set_page_config(
    page_title="Object Detection using YOLOv8",
    page_icon="Hi",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Object Detection using YOLOv8")

# Model Options
st.header("Select Task")
tasks = ['Object Detection', 'Object Measurement', 'Barcode Scanner']
model_type = st.radio("", tasks)

# Sidebar
#st.header("ML Model Config")

# Selecting Detection
model_path = Path(settings.DETECTION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

# # Object Detection Config
# st.header("Object Detection Config")
# source_radio = st.radio("Select Source", [settings.WEBCAM, settings.RTSP], key="source_radio_detection")


if model_type == 'Object Detection':
    source_radio = st.radio("Select Source", [settings.WEBCAM, settings.RTSP])
    
    if source_radio == settings.WEBCAM:
        if st.button('Detect Objects'):
            helper.play_webcam(model)
    
    elif source_radio == settings.RTSP:
        rtsp_url = st.text_input("Enter RTSP Stream URL for Detection:")
        if st.button('Detect Objects'):
            helper.play_rtsp_stream(model, rtsp_url)

elif model_type == 'Object Measurement':
    source_radio = st.radio("Select Source", [settings.WEBCAM, settings.RTSP])
    if source_radio == settings.WEBCAM:
        if st.button('Measure Objects'):
            helper.play_webcam(model)
    
    elif source_radio == settings.RTSP:
        rtsp_url = st.text_input("Enter RTSP Stream URL for Detection:")
        if st.button('Measure Objects'):
            helper.play_rtsp_stream(model, rtsp_url)

elif model_type == 'Barcode Scanner':
    source_radio = st.radio("Select Source", [settings.WEBCAM, settings.RTSP])
    if source_radio == settings.WEBCAM:
        if st.button('Scan Objects'):
            helper.play_webcam(model)
    
    elif source_radio == settings.RTSP:
        rtsp_url = st.text_input("Enter RTSP Stream URL for Detection:")
        if st.button('Scan Objects'):
            helper.play_rtsp_stream(model, rtsp_url)
