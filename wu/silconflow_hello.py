import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "deepseek-ai/DeepSeek-V3",
    "messages": [
        {
            "role": "user",
            "content":"You are a social media expert creating tweets for an audience interested in tiktok creator.  Write 5 engaging, concise, and visually appealing tweets that each: 1. Start with a compelling hook based on the following input: 'tips for tiktok creator' 2. Include the following call to action: '' 3. Use 2-3 relevant keywords/hashtags, including: 'tiktok,creator' 4. Adopt the following tone/style: 'Humorous' 5. Adhere to the following length requirement: Short (under 100 characters) Make sure to keep the tone consistent with the selected style and platform context.  Output each tweet separated by a newline.'}],You are a social media expert creating tweets for an audience interested in tiktok creator.  Write 5 engaging, concise, and visually appealing tweets that each: 1. Start with a compelling hook based on the following input: 'tips for tiktok creator' 2. Include the following call to action: '' 3. Use 2-3 relevant keywords/hashtags, including: 'tiktok,creator' 4. Adopt the following tone/style: 'Humorous' 5. Adhere to the following length requirement: Short (under 100 characters) Make sure to keep the tone consistent with the selected style and platform context.  Output each tweet separated by a newline.'You are a social media expert creating tweets for an audience interested in tiktok creator.  Write 5 engaging, concise, and visually appealing tweets that each: 1. Start with a compelling hook based on the following input: 'tips for tiktok creator' 2. Include the following call to action: '' 3. Use 2-3 relevant keywords/hashtags, including: 'tiktok,creator' 4. Adopt the following tone/style: 'Humorous' 5. Adhere to the following length requirement: Short (under 100 characters) Make sure to keep the tone consistent with the selected style and platform context.  Output each tweet separated by a newline."}
    ],
    "stream": False,
    "max_tokens": 512,
    "stop": ["null"],
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "frequency_penalty": 0.5,
    "n": 1,
    "response_format": {"type": "text"},
    "tools": [
        {
            "type": "function",
            "function": {
                "description": "<string>",
                "name": "<string>",
                "parameters": {},
                "strict": False
            }
        }
    ]
}
headers = {
    "Authorization": "Bearer sk-tqsduurfjnyvujddvusdmepgrpcdedsfcukvkniluzhtemgs",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)