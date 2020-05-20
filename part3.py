lda_model = gensim.models.LdaMulticore(corpus = corpus,
                                       id2word = id2word,
                                       num_topics = 10,
                                       random_state = 42,
                                       chunksize = 100,
                                       passes = 10,
                                       per_word_topics=True,
                                       minimum_probability = 0)
                                       
                                       
#save model in pickle format to working directory
lda_model.save("lda_putin.pkl")
#load model back into your workspace from working directory
lda_model = gensim.models.LdaModel.load("lda_putin.pkl")
