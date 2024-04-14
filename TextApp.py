import streamlit as st
from transformers import AutoTokenizer, AutoModelWithLMHead

# Load tokenizer and model
load_directory = "C:/Users/yaman/OneDrive/Desktop/Project Upgrad/Final/emotion_model"
tokenizer = AutoTokenizer.from_pretrained(load_directory)
model = AutoModelWithLMHead.from_pretrained(load_directory)

def get_emotion(text):
    input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')

    output = model.generate(input_ids=input_ids, max_length=2)

    dec = [tokenizer.decode(ids) for ids in output]
    label = dec[0]
    return label

def main():
    st.title("Emotion Detection App")
    text_input = st.text_area("Enter your text here:")
    
    if st.button("Analyse"):
        if text_input.strip() != "":
            emotion = get_emotion(text_input)
            st.write("Sentiment:", emotion)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
