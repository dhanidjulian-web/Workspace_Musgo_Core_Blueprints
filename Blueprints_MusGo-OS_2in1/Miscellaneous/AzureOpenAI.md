from openai import AzureOpenAI

# Azure OpenAI client for Azure-compatible endpoints
# Docs: https://github.com/openai/openai-python#microsoft-azure-openai
client = AzureOpenAI(
	api_key="your-secret-key",
	azure_endpoint="https://api.anyapi.ai",
	api_version="2024-10-21"
)

# request sent to model set on router, `router --model`
response = client.chat.completions.create(
	model="google/gemini-2.5-flash-lite",
	messages = []
)

print(response)