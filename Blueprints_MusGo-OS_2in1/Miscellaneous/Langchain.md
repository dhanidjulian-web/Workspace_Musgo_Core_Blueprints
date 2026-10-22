from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# ChatOpenAI with custom base_url for OpenAI-compatible APIs
# Docs: https://python.langchain.com/api_reference/openai/chat_models/
chat = ChatOpenAI(
    model="google/gemini-2.5-flash-lite",
    base_url="https://api.anyapi.ai",
    api_key="your-secret-key",
)

messages = [
    HumanMessage(content="Hello!")
]

response = chat.invoke(messages)
print(response.content)