from openai import OpenAI

# OpenAI client for OpenAI-compatible APIs
# Docs: https://github.com/openai/openai-python
client = OpenAI(
	api_key="your-secret-key",
	base_url="https://api.anyapi.ai"
)

# request sent to model set on router, `router --model`
response = client.chat.completions.create(
	model="google/gemini-2.5-flash-lite",
	messages = []
)

print(response)