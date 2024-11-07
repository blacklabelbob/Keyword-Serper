import bomber
import asyncio

# Set Your inputs
input_keyword = "Marketing Automation"
input_country = "US"

# Set your Open AI API Key
API_KEY = "sk-XXX"  # Replace with your actual OpenAI API key

# Run
try:
    asyncio.run(bomber.get_keyword_data(input_keyword, input_country, API_KEY))
except Exception as e:
    print(f"An error occurred: {e}")

# Indicate completion
print("Script execution completed.")
