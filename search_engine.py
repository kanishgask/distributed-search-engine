class SearchEngine:

    def __init__(self, index):
        self.index = index

    def search(self, query):
        tokens = query.lower().split()
        result_sets = []

        for token in tokens:
            result_sets.append(self.index.get(token, set()))

        if not result_sets:
            return []

        results = set.intersection(*result_sets)
        return list(results)


# Demo
if __name__ == "__main__":
    from indexer import InvertedIndex

    idx = InvertedIndex()
    idx.add_document(1, "Distributed systems are powerful")
    idx.add_document(2, "Search engines use inverted index")
    idx.add_document(3, "Distributed search engine design")

    engine = SearchEngine(idx.get_index())
    print(engine.search("distributed search"))
