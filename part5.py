#load lda model
lda_model = gensim.models.LdaModel.load("lda_putin.pkl")
#setup data-frame
weights_output = pd.DataFrame(columns = ['topic', 'prob_weight', 'doc_id'])
#setup progress bar
pbar = tqdm.tqdm(total = len(corpus))
#extraction loop
for i in range(0, len(corpus)):
    doc_weights = lda_model[corpus[i]][0]
    weights_df = pd.DataFrame(doc_weights, columns = ['topic', 'prob_weight'])
    weights_df['doc_id'] = i
    weights_output = weights_output.append(weights_df)
    pbar.update(1)
pbar.close()
#save information in the format you use
weights_output.to_csv("topic_weights_bydoc.csv")
weights_output.to_pickle("topic_weights_bydoc.pkl")
