from typing import Generator
from openai import OpenAI


class DeepSeekAI:
    def __init__(
            self, 
            api_key: str, 
            base_url: str = 'https://api.deepseek.com', 
        ):
        """
        DeepSeekAI
        api_key: str   密钥
        base_url: str   基础url
        """
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.models = {
            "chat": "deepseek-chat",
            "reason":"deepseek-reasoner"
        }


    def chat(self, model: str, messages: list[dict]) -> Generator[str, None, None]:
        """
        models:  chat/reason  
        messages: {"role": "user", "content": "Python 写冒泡排序法"}
        """
        try:
            response = self.client.chat.completions.create(
                model=self.models[model],
                messages=messages,
                stream=True
            )
            return response
        except Exception as e:
            print(e)
            return False
