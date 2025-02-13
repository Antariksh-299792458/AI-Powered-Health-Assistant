import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for advice"
    elif 'appointment' in user_input:
        return 'Would you like to schedule appointment with the doctor?'
    elif 'medication' in user_input:
        return "It's important to take prescribed medicines regularly."
    else:
        response = chatbot(user_input,max_length = 500,num_return_sequences = 1)
        return response[0]['generated_text']

def main():
    st.title("HealthCare Assistant Chatbot")
    user_input = st.text_input("How can i assist you?")
    if st.button('Submit'):
        if user_input:
            st.write('User :',user_input)
            with st.spinner('Processing Your Query. Please Wait ...'):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistance: ",response)
            print(response)
        else:
            st.write('Please enter a message ')


if __name__ == '__main__':
    main()