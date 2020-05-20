import pyLDAvis.gensim
import pickle
import pyLDAvis
import os
#first visualize the 10 topic model
LDAvis_data_filepath = os.path.join('./ldavis_prepared_'+str(10))
if 1 == 1:
LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
with open(LDAvis_data_filepath, 'w') as f:
        pickle.dump(LDAvis_prepared, f)
        
# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath) as f:
    LDAvis_prepared = pickle.load(f)
pyLDAvis.save_html(LDAvis_prepared, './ldavis_prepared_'+ str(10) +'.html')
