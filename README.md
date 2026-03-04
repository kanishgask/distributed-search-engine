# 🔎 Distributed Search Engine

> Day 9 – Scalable Search System

---

## 📌 Problem Statement

Design a distributed search engine that:

- Indexes documents
- Supports keyword search
- Returns ranked results
- Scales to millions of documents
- Supports horizontal scaling

---

# 🎯 Functional Requirements

- Add document
- Delete document
- Update document
- Search by keyword
- Return top-K results

---

# ⚙️ Non-Functional Requirements

- Low latency search (<200ms)
- Highly scalable
- Eventually consistent indexing
- Fault tolerant
- Horizontal sharding

---

# 🧠 Core Concepts

✔ Inverted index  
✔ Tokenization  
✔ Ranking (TF-IDF basic)  
✔ Sharding by document ID  
✔ Query fan-out  
✔ Aggregation of results  

---

# 📊 High-Level Flow

Write Path:
Client → API → Indexer → Shard → Store Index  

Read Path:
Client → API → Query Shards → Merge Results → Rank → Return  

---

# 🚀 Scale Assumption

- 1 Billion documents
- 100K search queries/sec
- Average 1KB per document

Heavy read optimization required.
