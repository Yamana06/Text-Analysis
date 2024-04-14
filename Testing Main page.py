import streamlit as st

# Center Aligning Function
def center_align():
    st.write("<style>div.Widget.row-widget.stRadio>div{flex-direction:row;justify-content:center}</style>", unsafe_allow_html=True)

# Page Title
st.title("Multimodal Sentiment Analysis")

# Center align the input type selection
center_align()

# Input Type Selection
input_type = st.radio("Select Input Type", ("Text", "Image", "Audio"))

# Team Members Section
st.subheader("About Team Members")
st.write("Pavan, Karthik, Abhiram, Ganesh")

# Clear page content for redirection
content_placeholder = st.empty()

# Page Routing based on Input Selection
if input_type == "Text":
    # Text Input Page
    st.write("Text Input Page Here")
elif input_type == "Image":
    # Redirect to Image Input Page
    st.write("Redirecting to Image Input Page...")
    st.experimental_rerun()
    st.text_input("Dummy Input")  # This is a dummy input to force Streamlit to rerun and redirect
elif input_type == "Audio":
    # Audio Input Page
    st.write("Audio Input Page Here")
