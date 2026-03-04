# 📊 ER Diagram - Search Engine

DOCUMENTS
- doc_id (PK)
- title
- content

INVERTED_INDEX
- term
- doc_id (FK)

Relationship:

Term N → N Documents
