from .GenerationEnums import GenerationEnums
from .providers import GroqGenerationProvider, OllamaGenerationProvider

class GenerationProviderFactory:
    def __init__(self, config: dict):
        self.config = config

    def create(self):
        provider = self.config.GENERATION_BACKEND
        if provider == GenerationEnums.GROQ.value:
            return GroqGenerationProvider(
                api_key = self.config.GROQ_API_KEY,
                model_id = self.config.GENERATION_MODEL_ID,
                default_input_max_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens=self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURE
            )

        if provider == GenerationEnums.OLLAMA.value:
            return OllamaGenerationProvider(
                api_url = self.config.OLLAMA_API_URL,
                model_id = self.config.GENERATION_MODEL_ID,
                default_input_max_characters=self.config.INPUT_DEFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens=self.config.GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=self.config.GENERATION_DEFAULT_TEMPERATURE
            )

        return None