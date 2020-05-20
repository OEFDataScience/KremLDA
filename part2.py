bigram = gensim.models.Phrases(df['Text'], min_count = 5,
                               threshold = 100)
bigram_mod = gensim.models.phrases.Phraser(bigram)

stop_words = stopwords.words('english')

#Remove stopwords
def remove_stopwords(texts):
    return[[word for word in simple_preprocess(str(doc)) if word not in stop_words]
            for doc in texts]
def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]
#Turn words into lemmas
def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB',
                                          'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if   token.pos_ in allowed_postags])
    return texts_out
    
    

data_words_nostops = remove_stopwords(df['Text'])

data_words_bigram = make_bigrams(data_words_nostops)

nlp = en_core_web_sm.load(disable = ['parser', 'ner'])
data_lemma = lemmatization(data_words_bigram, 
                           allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
                           
 #dictionary
id2word = corpora.Dictionary(data_lemma)
#corpus
texts = data_lemma
#term document matrix
corpus = [id2word.doc2bow(text) for text in texts]
