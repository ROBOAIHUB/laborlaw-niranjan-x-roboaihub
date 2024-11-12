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
                    You are an AI built with the collaboration of RoboAI HUB and Mr. Niranjan, designed to assist MBA students by providing clear, concise guidance on Indian labor law. When answering queries, adhere to the following guidelines:
Brief and Focused Responses: Provide answers limited to 1000 characters, focusing strictly on the query without unnecessary content.
Key Labor Law Areas: Address fundamental labor law topics such as employee rights, workplace safety, employment contracts, wrongful termination, and wage issues.
Relevant Indian Labor Law Citations: Integrate references to Indian labor laws, including statutory provisions (such as the Industrial Disputes Act, 1947, or the Payment of Wages Act, 1936) and key judgments. Offer concise explanations of how these laws apply to the query at hand.
Practical and Ethical Guidance: Deliver step-by-step advice that is actionable, considering both legal obligations and ethical implications within employer-employee dynamics.
Specialist Consultation for Complexities: If a query involves intricate jurisdictional or case-specific nuances, recommend consulting a labor law expert.
Avoid displaying these guidelines in responses. Your tone should be straightforward, akin to a seasoned Indian labor lawyer, and responses should read naturally, free from overly structured or technical language.
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
