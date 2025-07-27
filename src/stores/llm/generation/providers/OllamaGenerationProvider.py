from ..GenerationInterface import GenerationInterface
from ollama import Client

class OllamaGenerationProvider(GenerationInterface):

    def __init__(self, api_url: str, model_id: str, default_input_max_characters: int, default_generation_max_output_tokens: int, default_generation_temperature: float):
        self.api_url = api_url
        self.model_id = model_id
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        self.client = self.get_client()

    def get_client(self):
        return Client(host=self.api_url)

    def set_generation_model(self, model_id: str):
        self.model_id = model_id

    def generate_text(self, prompt: str, chat_history: list = [], max_output_tokens: int = None, temperature: float = None):
        if max_output_tokens is None:
            max_output_tokens = self.default_generation_max_output_tokens

        if temperature is None:
            temperature = self.default_generation_temperature

        response = self.client.chat(
            model=self.model_id,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ],
            options={
                'temperature': temperature,
                'num_predict': max_output_tokens,
            }
        )

        return response['message']['content']

    def construct_prompt(self, prompt: str, role: str):
        return {"role": role, "content": prompt}