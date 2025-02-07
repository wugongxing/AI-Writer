import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key= "sk-44662644fd764a0f991e3c1ea732e006", #os.getenv("sk-44662644fd764a0f991e3c1ea732e006"), 
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-max", # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[
        {'role': 'user', 'content': 'You are a social media expert creating tweets for an audience interested in tiktok creator.  Write 5 engaging, concise, and visually appealing tweets that each: 1. Start with a compelling hook based on the following input: "tips for tiktok creator" 2. Include the following call to action: "" 3. Use 2-3 relevant keywords/hashtags, including: "tiktok,creator" 4. Adopt the following tone/style: "Humorous" 5. Adhere to the following length requirement: Short (under 100 characters) Make sure to keep the tone consistent with the selected style and platform context.  Output each tweet separated by a newline.'}],
    )
    
print(completion.model_dump_json())