CREATE TABLE documents (
    doc_id UUID PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inverted_index (
    term VARCHAR(255),
    doc_id UUID REFERENCES documents(doc_id),
    PRIMARY KEY (term, doc_id)
);
