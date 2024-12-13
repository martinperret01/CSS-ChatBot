import os
import streamlit as st
from openai import OpenAI

# Set your OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("Please set the OPENAI_API_KEY environment variable.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Function to query OpenAI API
def query_openai(prompt):
    try:
        # Generate a chat completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if needed
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,  # Limit response size
            temperature=0.7  # Adjust creativity
        )
        # Access the content of the first choice
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app interface
st.title("ChatBot for NP Customer Success Stories")

# Input box for user prompt
prompt = st.text_input("Enter your question or prompt below:")

# Submit button
if st.button("Submit"):
    if prompt:
        with st.spinner("Generating response..."):
            response = query_openai(prompt)
        st.write("**Response:**")
        st.write(response)
    else:
        st.warning("Please enter a prompt.")
