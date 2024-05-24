import streamlit as st

from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage


class ChatHistory:
    def __init__(self):
        self.history = st.session_state.get("history",
                                            ConversationBufferMemory(memory_key="chat_history", return_messages=True))
        st.session_state["history"] = self.history

    def default_greeting(self):
        return "Hi ! 👋"

    def default_prompt(self, topic):
        return f"Hello ! Ask me anything about {topic} 🤗"

    def initialize(self, topic):
        st.message(self.default_greeting(), key='hi', avatar_style="adventurer", is_user=True)
        st.message(self.default_prompt(topic), key='ai', avatar_style="thumbs")

    def reset(self):
        st.session_state["history"].clear()
        st.session_state["reset_chat"] = False

    def generate_messages(self, container):
        if st.session_state["history"]:
            with container:
                messages = st.session_state["history"].chat_memory.messages
                for i in range(len(messages)):
                    msg = messages[i]
                    if isinstance(msg, HumanMessage):
                        st.message(
                            msg.content,
                            is_user=True,
                            key=f"{i}_user",
                            avatar_style="adventurer",
                        )
                    elif isinstance(msg, AIMessage):
                        st.message(msg.content, key=str(i), avatar_style="thumbs")
