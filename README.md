# J.A.R.V.I.S - AI Powered Personal Assistant

**Jarvis** is an AI-powered personal assistant designed to provide contextual answers about my education, projects, experience, skills, and background. It integrates a **document ingestion pipeline**, a **RAG-based backend**, and an **interactive frontend**, demonstrating how modern AI systems are designed and orchestrated for real-world applications.

This project was created to learn modern AI engineering concepts, RAG pipelines, vector search, embeddings, worker queues, service orchestration, while building a chatbot experience for my portfolio.

## System Overview

Jarvis is composed of three interconnected components:

### 1. Jarvis UI [🔗](https://github.com/akshayrpatel/akshayrpatel.github.io/tree/v4.0/components/jarvis)

The frontend provides an interactive chat interface and is built with Next.js, React + TypeScript, and Tailwind.

Key features include:

- Allows visitors to submit queries to the backend
- Displays real-time, context-aware AI responses
- Provides a responsive and accessible user experience across devices

### 2. Jarvis LangChain Server [🔗](https://github.com/akshayrpatel/jarvis-langchain-server/tree/v1.1)

The backend implements a RAG pipeline and processes all project-related documents, converting them into embeddings to support semantic search.

Key features include:

- Classifies queries for targeted document retrieval
- Retrieves context from a vector database
- Orchestrates multi-provider LLM calls with failover
- Maintains per-session conversation history
- Generates accurate and coherent responses

### 3. Jarvis ETL Data Pipeline [🔗](https://github.com/akshayrpatel/jarvis-etl)

The ETL pipeline processes all project-related documents and converts them into embeddings to support semantic search.

Key responsibilities include:

- Loading and parsing multiple document formats (PDF, Markdown, text, HTML)
- Chunking documents into semantically meaningful units
- Generating embeddings using embedding models
- Storing embeddings in a vector database for fast retrieval

The pipeline uses a threaded producer–consumer model with Redis backed queues to enable scalable and fault-tolerant processing.

## Architecture

The system architecture is modular, with clearly defined responsibilities for each component:

- **Frontend UI**: Handles user interaction and manages chat sessions
- **Langchain Backend Server**: MemoryService, CategoryClassifier, VectorDBService, LLMService, RAGService, ServiceRegistry
- **ETL Pipeline**: DocumentService, DocumentWorker, EmbeddingWorker, VectorDBWorker, RedisBufferQueue, Pipeline Orchestrator

The components interact as follows:

1. Documents are ingested, chunked, and embedded by the ETL pipeline
2. Embeddings are stored in a vector database (ChromaDB)
3. The LangChain server retrieves relevant chunks and generates responses using LLMs
4. The frontend displays responses to the user in a structured chat interface

This architecture ensures separation of concerns, maintainability, and reliability in both data processing and user interaction.

## Features

- Real-time, context-aware AI responses
- Semantic search over custom knowledge base
- Modular service design for maintainability
- Multi-provider LLM orchestration with failover
- Threaded ETL pipeline for document ingestion and embedding generation
- Responsive and interactive chat interface

## Technologies and Concepts

### Frontend

- Next.js
- React + TypeScript
- TailwindCSS

### Backend

- Python 3
- FastAPI, Uvicorn
- LangChain
- ChromaDB
- Multi-provider LLM integration (OpenAI, Mistral, Groq)
- Async programming and prompt template design

### ETL Pipeline

- Python 3
- Redis (queueing backend)
- Threaded producer–consumer model
- SentenceTransformers / FastEmbed for embeddings
- Events for signaling termination
- Service-oriented modular architecture

### Key Concepts

- Retrieval-Augmented Generation (RAG)
- Vector search and embeddings
- Session memory management
- Modular, testable service design
- Thread coordination and clean shutdown with sentinels
- Pipeline orchestration

## Challenges and Learnings

During development, several technical challenges were addressed:

- Designing and orchestrating a full RAG pipeline
- Implementing multi-threaded workers with Redis queues and sentinels
- Handling asynchronous calls and failover across multiple LLM providers
- Chunking documents and generating embeddings for semantic search
- Integrating frontend, backend, and ETL components into a cohesive system

The project enhanced skills in AI engineering, systems engineering, full-stack development, and production-grade software design.

## Future Improvements

- Integrating agentic workflows
- Enhanced prompt engineering and context handling
- Automated ingestion of new documents and knowledge updates
