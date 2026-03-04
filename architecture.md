# 🏗️ Distributed Search Architecture

Client
   ↓
API Gateway
   ↓
Search Coordinator
   ↓
Shard 1   Shard 2   Shard 3
   ↓         ↓         ↓
Index Store  Index Store  Index Store

---

# Write Path

1. Document received
2. Tokenization
3. Inverted index updated
4. Shard chosen via hash(doc_id)

---

# Read Path

1. Query received
2. Broadcast to all shards
3. Each shard returns top-K
4. Coordinator merges & ranks

---

# Scaling Strategy

- Shard by doc_id
- Replicate shards
- Cache hot queries (Redis)
- Separate indexing pipeline

---

# Failure Handling

If shard fails:
- Query replica
- Index rebuild from log

---

# Improvements

- TF-IDF ranking
- Phrase search
- Fuzzy matching
- Autocomplete
- Geo-search
