import logging

from typing import List
from langchain_core.messages import SystemMessage, HumanMessage

from app.config.services import classifier_config
from app.services.category_classifier import CategoryClassifier
from app.services.memory_service import MemoryService
from app.services.vectordb_service import VectorDBService
from app.services.llm_service import LLMService
from app.templates.generic_template import RAG_TEMPLATE

logger = logging.getLogger(__name__)


class RAGService:
	"""
	Retrieval-Augmented Generation (RAG) pipeline for answering user queries.

  This service orchestrates:
  1. Storing the conversation history in memory.
  2. Classifying the user's query to determine relevant categories.
  3. Retrieving contextually relevant documents from the vector database.
  4. Constructing a RAG-formatted prompt.
  5. Querying the LLM.
  6. Returning the generated answer.

  Attributes:
      memory_service (``MemoryService``): Stores and retrieves conversation history.
      vectordb_service (``VectorDBService``): Performs similarity search on vector data.
      llm_service (``LLMService``): Sends messages to LLM providers and gets responses.
      classifier (``CategoryClassifier``): Classifies user queries into categories for
          category-aware vector search.
  """

	def __init__(self,
	             memory: MemoryService,
	             vectordb: VectorDBService,
	             llm: LLMService):
		self.memory_service = memory
		self.vectordb_service = vectordb
		self.llm_service = llm
		self.classifier = CategoryClassifier(classifier_config.model_local)

	async def _retrieve_context(self, query: str) -> str | None:
		# logger.debug("[RAGService] Retrieving context for query: %s", query)
		# try:
		# 	input_query_embedding: List[float] = self.embedding_service.get_embedding(query)
		# 	relevant_docs: List[str] = self.vectordb_service.similarity_search(query, input_query_embedding, k = k)
		# except Exception as e:
		# 	logger.error("[RAGService] Failed to retrieve context: %s", e)
		# 	return None
		logger.info("[RAGService] Retrieving context for query: %s", query)
		try:
			categories: List[str] = self.classifier.classify(query)
			relevant_docs: List[str] = self.vectordb_service.similarity_search_by_category(query, categories)
		except Exception as e:
			logger.error("[RAGService] Failed to retrieve context: %s", e)
			return None

		if not relevant_docs:
			logger.info("[RAGService] No context found for query: %s", query)
			return None

		context =  "\n".join(doc for doc in relevant_docs)
		logger.info("[RAGService] Retrieved context: ...%s", context[:100])
		return context

	async def answer(self, session_id: str, query: str) -> str:
		"""
    Add current query to memory, retrieve message from history, get relevant documents and answer
    """

		# save query to memory
		self.memory_service.add_user_message(session_id, query)

		# retrieve conversation history as messages
		history_messages = self.memory_service.load_messages(session_id)

		# get relevant document context
		context = await self._retrieve_context(query)

		formatted_prompt = RAG_TEMPLATE.format(
			context=context or "No useful context found.",
			question=query,
		)

		messages = [
			SystemMessage(content="You are Jarvis, my personal AI assistant."),
			*history_messages,
			HumanMessage(content=formatted_prompt),
		]

		logger.info("[RAGService] Sending query to LLM: %s", query)
		response =  await self.llm_service.chat(messages)
		logger.info("[RAGService] Received response from LLM: ... %s", response[:50])

		return response
