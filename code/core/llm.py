import requests
import json
from config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL

class DeepSeekLLM:
    def __init__(self, api_key=None):
        self.api_key = api_key or DEEPSEEK_API_KEY
        self.api_url = DEEPSEEK_API_URL
        
    def generate_response(self, messages, model="deepseek-chat", temperature=0.7, max_tokens=4000):
        """
        使用DeepSeek API生成响应
        
        Args:
            messages: 消息历史列表，格式为[{"role": "user", "content": "..."}, ...]
            model: 使用的模型名称
            temperature: 温度参数，控制随机性
            max_tokens: 最大生成令牌数
            
        Returns:
            生成的响应文本
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error calling DeepSeek API: {e}")
            return f"Sorry, I encountered an error: {str(e)}"