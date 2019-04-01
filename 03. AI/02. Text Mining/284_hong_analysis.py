from gensim.models import word2vec

model = word2vec.Word2Vec.load("hong.model")

print(model.most_similar(positive=["대통령"]))