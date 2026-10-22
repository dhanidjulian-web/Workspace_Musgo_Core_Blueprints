from llama_index.llms.openai_like import OpenAILike
from llama_index.core.llms import ChatMessage

# OpenAILike for OpenAI-compatible APIs (custom endpoints)
# Docs: https://docs.llamaindex.ai/en/stable/api_reference/llms/openai_like/
llm = OpenAILike(
    model="google/gemini-2.5-flash-lite",
    api_base="https://api.anyapi.ai",
    api_key="your-secret-key",
    is_chat_model=True,
)

messages = [
    ChatMessage(role="user", content="Hello!")
]

response = llm.chat(messages)
print(response)