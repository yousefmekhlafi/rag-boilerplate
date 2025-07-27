from ..GenerationInterface import GenerationInterface
import cohere

class CoHereGenerationProvider(GenerationInterface):

    def __init__(self, api_key: str, model_id: str, default_input_max_characters: int, default_generation_max_output_tokens: int, default_generation_temperature: float):
        self.api_key = api_key
        self.model_id = model_id
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        self.client = self.get_client()

    def get_client(self):
        return cohere.Client(self.api_key)

    def set_generation_model(self, model_id: str):
        self.model_id = model_id

    def generate_text(self, prompt: str, chat_history: list = [], max_output_tokens: int = None, temperature: float = None):
        if max_output_tokens is None:
            max_output_tokens = self.default_generation_max_output_tokens

        if temperature is None:
            temperature = self.default_generation_temperature

        response = self.client.chat(
            model=self.model_id,
            message=prompt,
            temperature=temperature,
            max_tokens=max_output_tokens
        )

        return response.text

    def construct_prompt(self, prompt: str, role: str):
        return {"role": role, "content": prompt}