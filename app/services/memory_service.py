import logging

from typing import Dict
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

logger = logging.getLogger(__name__)


class MemoryService:
	"""
	Session-based conversation memory using LangChain's in-memory message history.

  This service manages chat histories for multiple user sessions. Each session
  is stored in an ``InMemoryChatMessageHistory`` object, which holds a sequence
  of ``HumanMessage`` and ``AIMessage`` entries. The memory persists only for
  the lifetime of the server instance (i.e., it is not persisted to disk).

  Attributes:
      store (Dict[str, InMemoryChatMessageHistory]):
          A mapping from session IDs to their corresponding chat histories.
  """

	def __init__(self):
		self.store: Dict[str, InMemoryChatMessageHistory] = {}

	def get_history(self, session_id: str) -> InMemoryChatMessageHistory:
		if session_id not in self.store:
			self.store[session_id] = InMemoryChatMessageHistory()
		return self.store[session_id]

	def add_user_message(self, session_id: str, text: str):
		history = self.get_history(session_id)
		history.add_message(HumanMessage(content=text))

	def add_ai_message(self, session_id: str, text: str):
		history = self.get_history(session_id)
		history.add_message(AIMessage(content=text))

	def load_messages(self, session_id: str):
		return self.get_history(session_id).messages
