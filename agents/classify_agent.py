from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def classify_topic(text, topic_list):
    vectorizer = TfidfVectorizer().fit(topic_list + [text])
    vectors = vectorizer.transform(topic_list + [text])
    similarities = cosine_similarity(vectors[-1], vectors[:-1])
    return topic_list[similarities.argmax()]
