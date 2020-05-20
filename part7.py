#this code can help with identifying difference in topic ordering
#between gensim model and LDAvis
vis_data = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
print(vis_data.topic_order)
#[2, 7, 3, 6, 5, 8, 9, 4, 1, 10]

#create topic labels for data-set
topic_labels = ['Sport and culture', "Domestic politics", "Economy", "Crime and punishment", "Military/Defense", "Nationalism", 
                "Diplomacy and trade", "Oil and energy", "Regional politics", "Human development"]
topic_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data_tuple = list(zip(topic_id, topic_labels))
df_labels = pd.DataFrame(data_tuple, columns = ['topic', 'topic_label'])
#merge labels into year weights data
df_avg2 = df_avg.merge(df_labels, on='topic')
#save
df_avg2.to_csv("year_topic_weights.csv")

#now create a final per-document data-frame for broader analysis
df12 = pd.merge(df4,df_avg2[['year', 'topic', 'average_weight', 'total_docs', 'topic_label']],on=['year', 'topic'], how='left')
df12.to_csv("FULL_PUTIN_PROCESSED.csv")
df12.to_pickle("FULL_PUTIN_PROCESSED.pkl")
