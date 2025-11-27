from pydantic import BaseModel
from app.config.settings import settings

class MistralConfig(BaseModel):
	api_key: str = settings.mistral_api_key
	model: str = settings.mistral_model_name
	model_embed: str = settings.mistral_model_embed_name
	temperature: float = 0.5
	max_retries: int = 2

class GroqConfig(BaseModel):
	api_key: str = settings.groq_api_key
	model: str = settings.groq_model_name
	temperature: float = 0.5
	max_retries: int = 2

class OpenRouterConfig(BaseModel):
	api_key: str = settings.openrouter_api_key
	model: str = settings.openrouter_model_name
	base_url: str = settings.openrouter_base_url
	temperature: float = 0.5
	max_retries: int = 2

mistral_config = MistralConfig()
groq_config = GroqConfig()
openrouter_config = OpenRouterConfig()
