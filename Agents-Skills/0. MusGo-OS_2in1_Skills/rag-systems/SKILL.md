---
name: rag-systems
description: "Guides designing, implementing, and evaluating production-grade RAG systems, emphasizing retrieval quality, chunking, indexing, and metadata-driven filtering."
metadata:
  tags: "ai, rag, retrieval-augmented-generation, system-design, document-processing, indexing, evaluation"
  source: "https://skilldb.dev/skills/data-ai-skills/rag-systems"
  pack: "data-ai-skills"
  category: "Technology & Engineering"
---

# RAG Systems Architect

## When to use this skill
Use when the user says things like:
- "How do I design a RAG system?"
- "Help me architect a retrieval augmented generation pipeline."
- "I need guidance on RAG architecture best practices."
- "Evaluate my RAG retrieval setup."
- "How can I improve retrieval quality in my RAG system?"


You are a senior AI engineer who specializes in building production RAG systems. You have learned that retrieval quality determines answer quality — a perfect language model with bad retrieval produces bad answers. You focus on the boring fundamentals: chunking, indexing, and evaluation. You are skeptical of "just throw it in a vector database" approaches.

## Philosophy

RAG is an information retrieval problem, not a language model problem. The LLM is the last mile — if you retrieve the wrong documents, no amount of prompt engineering will produce correct answers. Spend 80% of your effort on retrieval quality and 20% on generation.

The most common failure in RAG systems is not technical — it is skipping evaluation. Teams build a pipeline, try five queries manually, declare success, and deploy. Then users find the system confidently wrong on basic questions. Build evaluation into your pipeline from day one.

## RAG Architecture

### The Core Pipeline

```
Documents -> Chunking -> Embedding -> Index -> Query -> Retrieve -> Rerank -> Generate -> Answer
```

Each stage has failure modes. Understand them.

### Stage 1: Document Processing

Before chunking, you must extract clean text from source documents.

```python
# Document processing priorities
processing_checklist = {
    "PDF": "Use a layout-aware parser (not just text extraction). Tables, headers, and columns matter.",
    "HTML": "Strip boilerplate (nav, footer, ads). Preserve semantic structure (headers, lists).",
    "Code": "Preserve syntax structure. Chunk by function/class, not by character count.",
    "Markdown": "Chunk by section headers. Preserve header hierarchy in metadata.",
    "Slides": "Each slide is a natural chunk. Include slide title as metadata.",
}
```

Critical: preserve metadata through the pipeline. Source document, page number, section title, last updated date — this metadata is essential for filtering, attribution, and debugging.

### Stage 2: Chunking Strategies

Chunking determines retrieval quality more than embedding model choice.

#### Fixed-Size Chunking
```python
# Simple but effective baseline
chunk_size = 512  # tokens
chunk_overlap = 64  # tokens

# Rule of thumb: chunk size should match your typical query's answer span.
# If answers are usually 1-2 paragraphs, chunks of 256-512 tokens work well.
# If answers require full-page context, use 1024+ tokens.
```

#### Semantic Chunking
```python
# Split at natural boundaries: paragraphs, sections, topic shifts
def semantic_chunk(text, max_tokens=512):
    paragraphs = text.split('\
\
')
    chunks = []
    current_chunk = []
    current_size = 0

    for para in paragraphs:
        para_tokens = count_tokens(para)
        if current_size + para_tokens > max_tokens and current_chunk:
            chunks.append('\
\
'.join(current_chunk))
            current_chunk = [para]
            current_size = para_tokens
        else:
            current_chunk.append(para)
            current_size += para_tokens

    if current_chunk:
        chunks.append('\
\
'.join(current_chunk))
    return chunks
```

#### Hierarchical Chunking
```
Document -> Sections -> Paragraphs

Store at multiple levels:
- Section-level chunks for broad context retrieval
- Paragraph-level chunks for precise answer retrieval
- Link child chunks to parent chunks for context expansion
```

#### Chunking Rules

1. Never split mid-sentence. Sentence boundaries are a hard minimum.
2. Include context in each chunk: prepend the section header or document title.
3. Tables should be kept as complete units. A half-table is useless.
4. Code blocks must never be split. A partial function is worse than no function.
5. Overlap is important. 10-15% overlap prevents losing information at boundaries.

### Stage 3: Embedding

```python
# Embedding model selection factors
considerations = {
    "dimension_size": "Higher dims = more expressive but more storage. 768-1536 is typical.",
    "max_token_length": "Must exceed your chunk size. Truncation silently kills quality.",
    "domain_match": "General-purpose models work for most cases. Domain-specific models help for specialized vocabularies.",
    "query_vs_document": "Some models use different prefixes for queries vs documents. Use them.",
}

# Always normalize embeddings for cosine similarity
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('BAAI/bge-large-en-v1.5')

# Note the instruction prefix for query embeddings
query_embedding = model.encode("Represent this sentence for searching relevant passages: " + query)
doc_embedding = model.encode(chunk_text)
```

### Stage 4: Indexing and Vector Database

```python
# Index configuration that matters
index_config = {
    "index_type": "HNSW",  # Best quality/speed tradeoff for most use cases
    "ef_construction": 200,  # Higher = better quality index, slower build
    "M": 16,  # Number of connections per node. 12-48 typical.
    "ef_search": 128,  # Higher = better recall, slower query
    "distance_metric": "cosine",  # Match your embedding model's training
}
```

Store metadata alongside vectors. You will need it for filtering.

```python
# Metadata to store with each chunk
metadata = {
    "source_document": "product_manual_v3.pdf",
    "page_number": 42,
    "section_title": "Troubleshooting Network Errors",
    "document_type": "manual",
    "last_updated": "2025-06-15",
    "access_level": "public",
    "chunk_index": 7,
    "total_chunks": 23,
}
```

### Stage 5: Retrieval

#### Hybrid Search

Combine semantic search (vector similarity) with keyword search (BM25). This is almost always better than either alone.

```python
def hybrid_search(query, top_k=10, alpha=0.7):
    """
    alpha: weight for semantic search (1.0 = pure semantic, 0.0 = pure keyword)
    Typical sweet spot: 0.6-0.8 for general use cases
    """
    semantic_results = vector_db.search(embed(query), top_k=top_k * 2)
    keyword_results = bm25_index.search(query, top_k=top_k * 2)

    # Reciprocal Rank Fusion
    combined = reciprocal_rank_fusion(
        [semantic_results, keyword_results],
        weights=[alpha, 1 - alpha]
    )
    return combined[:top_k]
```

#### Metadata Filtering

Apply filters before or during vector search to narrow the search space.

```python
# Filter by document type and recency
results = vector_db.search(
    query_embedding,
    filter={
        "document_type": {"$in": ["manual", "faq"]},
        "last_updated": {"$gte": "2024-01-01"},
        "access_level": {"$eq": user.access_level},
    },
    top_k=10
)
```

#### Query Transformation

The user's query is often not the best search query. Transform it.

```python
transformations = [
    "Rewrite the query as a declarative statement (questions search poorly)",
    "Generate 2-3 alternative phrasings for broader recall",
    "Extract key entities and search for them specifically",
    "Decompose multi-part questions into sub-queries",
]

# Example: HyDE (Hypothetical Document Embedding)
# Generate a hypothetical answer, embed that, search with it
hypothetical_answer = llm("Write a short paragraph that would answer: " + query)
hyde_embedding = embed(hypothetical_answer)
results = vector_db.search(hyde_embedding, top_k=10)
```

### Stage 6: Reranking

Initial retrieval optimizes for recall. Reranking optimizes for precision.

```python
from sentence_transformers import CrossEncoder
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-12-v2')

# Rerank top results with a cross-encoder
pairs = [(query, chunk.text) for chunk in initial_results]
scores = reranker.predict(pairs)
reranked = sorted(zip(initial_results, scores), key=lambda x: x[1], reverse=True)
final_results = [r for r, s in reranked[:5]]
```

### Stage 7: Generation

```python
generation_prompt = """Answer the question based ONLY on the provided context.
If the context does not contain enough information to answer, say "I don't have
enough information to answer this question" and explain what information is missing.

Context:
{chunks}

Question: {query}

Rules:
- Cite your sources using [Source: document_name, page X] format
- Do not use any information not present in the context
- If different sources contradict each other, note the contradiction
"""
```

## Evaluation Framework

### Retrieval Metrics

- **Recall@k**: Of the relevant documents, how many appear in the top k results?
- **Precision@k**: Of the top k results, how many are relevant?
- **MRR (Mean Reciprocal Rank)**: Where does the first relevant result appear on average?

### End-to-End Metrics

- **Faithfulness**: Does the answer only use information from retrieved documents?
- **Answer relevance**: Does the answer address the user's question?
- **Context relevance**: Are the retrieved documents relevant to the question?

```python
# Build an eval set: question, expected answer, relevant source documents
eval_set = [
    {
        "question": "How do I reset my password?",
        "expected_answer": "Go to Settings > Security > Reset Password",
        "relevant_docs": ["user_guide_v2.pdf"],
        "relevant_pages": [15],
    },
    # ... 50+ test cases covering common and edge-case queries
]
```

## Anti-Patterns

- **Chunk and pray**: Using default chunk sizes without testing different strategies. Chunking is the highest-leverage optimization.
- **Ignoring hybrid search**: Pure vector search misses exact keyword matches. Always combine with BM25 or similar.
- **No evaluation set**: "It works on my five test queries" is not evaluation. Build a comprehensive test set.
- **Stuffing the context**: Retrieving 20 chunks and stuffing them all into the prompt. More context is not better — it dilutes relevant information.
- **Ignoring metadata**: Not storing or using metadata for filtering. Metadata filters are often more effective than better embeddings.
- **One-size-fits-all chunking**: Using the same chunk size for code, prose, tables, and FAQs. Different content types need different strategies.
- **Skipping reranking**: Initial retrieval with approximate nearest neighbors has limited precision. A reranker is cheap and dramatically improves quality.
- **Not handling updates**: Building a system that cannot incrementally update when source documents change. Plan for document lifecycle from the start.