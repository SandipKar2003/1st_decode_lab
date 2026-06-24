import streamlit as st
from given import KNOWN
from llm import ask_llm

st.set_page_config(
    page_title="Hybrid AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

.main {
    background-color: #ece5dd;
}

.user-message {
    background-color: #dcf8c6;
    padding: 12px;
    border-radius: 12px;
    margin: 8px;
    text-align: right;
}

.bot-message {
    background-color: white;
    padding: 12px;
    border-radius: 12px;
    margin: 8px;
    text-align: left;
}

</style>
""", unsafe_allow_html=True)

st.title("Hybrid AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []


def get_response(user_input):

    user_input = user_input.lower().strip()

    known_response = KNOWN.get(user_input)

    if known_response:
        return known_response

    return ask_llm(user_input)


for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f"""
            <div class='user-message'>
            {msg['content']}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class='bot-message'>
            {msg['content']}
            </div>
            """,
            unsafe_allow_html=True
        )


user_prompt = st.chat_input("Type your message...")

if user_prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    response = get_response(user_prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()