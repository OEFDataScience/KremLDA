df = pd.read_pickle("topic_weights_bydoc.pkl")
df2 = pd.read_pickle("putin_scrape.pkl")

df3 = df2.reset_index()
df3['doc_id'] = df3.index
df3['year'] = pd.DatetimeIndex(df3['Date']).year

df4 = pd.merge(df,df3[['doc_id','year', 'Transcript Title', 'Text', 'URL', 'Date']],on='doc_id', how='left')
total_docs = df4.groupby('year')['doc_id'].apply(lambda x: len(x.unique())).reset_index()
total_docs.columns = ['year', 'total_docs']
total_docs.to_csv("total_doc_year.csv")
df_avg = df4.groupby(['year', 'topic']).agg({'prob_weight':'sum'}).reset_index()
df_avg = df_avg.merge(total_docs, on='year', how="left")
df_avg['average_weight'] = df_avg['prob_weight'] / df_avg['total_docs']
