class SearchEngine:
    def __init__(self):
        self.index = {}

    def add_document(self, id, text):
        self.index[id] = text

    def search(self, query):
        results = []
        for id, text in self.index.items():
            if query.lower() in text.lower():
                results.append(id)
        return results

class Indexer:
    def __init__(self):
        self.search_engine = SearchEngine()

    def add_document(self, id, text):
        self.search_engine.add_document(id, text)

    def search(self, query):
        return self.search_engine.search(query)

class SearchInterface:
    def __init__(self, indexer):
        self.indexer = indexer

    def add_document(self, id, text):
        self.indexer.add_document(id, text)

    def search(self, query):
        return self.indexer.search(query)

# Test
indexer = Indexer()
interface = SearchInterface(indexer)

interface.add_document("doc1", "This is a sample document.")
interface.add_document("doc2", "Another document for testing.")

print(interface.search("document"))  # [doc1, doc2]
print(interface.search("sample"))  # [doc1]
print(interface.search("non-existent"))  # []
