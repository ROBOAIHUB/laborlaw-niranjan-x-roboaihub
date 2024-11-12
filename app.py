import streamlit as st
import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("API_KEY")

# Initialize the Streamlit app title and disclaimer
st.title("Trial Chatbot on Labour Laws for MBA students : Niranjan × RoboAI")
st.text("""Disclaimer: This is an experimental trial on the use of AI for educational purposes only, using open source material. Oct 2023.""")

# Initialize the session state for messages if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("Ask questions related to Labor Law"):
    # Append the user's input to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display the user's input in chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate the response from the OpenAI model
    with st.chat_message("Legal Advisor"):
        try:
            # OpenAI API call to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": """
                    Respond like a seasoned Indian labor lawyer, with collaboration from RoboAI HUB and Mr. Niranjan, designed to assist MBA students. For each query, analyze labor law issues in the Indian context, covering key aspects like employee rights, workplace safety, and employment contracts. Cite relevant Indian labor law judgments and statutory provisions, explaining their implications concisely. Provide practical, step-by-step guidance with clear legal and ethical insights, especially regarding employer-employee dynamics, including workplace disputes, wrongful termination, and wage-related issues. If there are complexities that may vary by jurisdiction, recommend consulting a labor law expert. Keep responses concise, professional, and easy to understand
                    """},
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract and display the model's response
            response_content = response.choices[0].message['content']
            st.markdown(response_content)
            
            # Append the assistant's response to session state
            st.session_state.messages.append({"role": "assistant", "content": response_content})
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
