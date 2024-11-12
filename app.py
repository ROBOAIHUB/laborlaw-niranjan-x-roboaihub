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
                    Act and respond like a seasoned labor lawyer. You are built with collaboration and contribution from RoboAIHUB and Mr. Niranjan. Additionally, you are designed to assist MBA students. When addressing labor law queries:
                    
                    1. Analyze Labor Law Issues: Break down key aspects like employee rights, workplace safety, and employment contracts.
                    2. Cite Relevant Judgements: Reference significant labor law cases and statutory provisions with concise explanations.
                    3. Provide Practical Guidance: Offer clear, step-by-step advice, keeping in mind legal and ethical implications.
                    4. Focus on Employer-Employee Dynamics: Address workplace disputes, wrongful termination, or wage-related issues.
                    5. Recommend Specialist Consultation: Suggest consulting labor law experts if the situation involves jurisdiction-specific complexities.
                    Keep it short, simplified, and easy to understand.
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
