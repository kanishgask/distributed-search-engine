import re
from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def add_document(self, doc_id, text):
        words = self.tokenize(text)
        for word in words:
            self.index[word].add(doc_id)

    def remove_document(self, doc_id):
        for word in self.index:
            self.index[word].discard(doc_id)

    def get_index(self):
        return self.index
