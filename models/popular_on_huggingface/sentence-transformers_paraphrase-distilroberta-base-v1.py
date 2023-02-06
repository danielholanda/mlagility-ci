# labels: test_group::monthly author::sentence-transformers name::paraphrase-distilroberta-base-v1 downloads::10,933 license::apache-2.0 task::Sentence_Similarity
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/paraphrase-distilroberta-base-v1')
embeddings = model.encode(sentences)
print(embeddings)
