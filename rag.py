from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class KnowledgeBase:

    def __init__(self):
        self.chunks = []
        self.sources = []
        self.vectorizer = None
        self.vectors = None

    def add_document(self, text, source):

        words = text.split()
        chunk_size = 250

        for i in range(0, len(words), chunk_size):

            chunk = " ".join(words[i:i + chunk_size])

            if chunk.strip():

                self.chunks.append(chunk)
                self.sources.append(source)

        if self.chunks:

            self.vectorizer = TfidfVectorizer(
                stop_words="english"
            )

            self.vectors = self.vectorizer.fit_transform(
                self.chunks
            )

    def search(self, question, top_k=5):

        if not self.chunks:
            return []

        question_vector = self.vectorizer.transform(
            [question]
        )

        scores = cosine_similarity(
            question_vector,
            self.vectors
        )[0]

        ranked_indexes = scores.argsort()[::-1]

        results = []

        for index in ranked_indexes[:top_k]:

            results.append({
                "text": self.chunks[index],
                "source": self.sources[index],
                "score": float(scores[index])
            })

        return results