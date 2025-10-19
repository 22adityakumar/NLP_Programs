import pandas as pd
import numpy as np
corpus = ['data science is one of the most important fields of science',
'this is one of the best data science coures',
'data scientists analyze data' ]
words_set = set()
for doc in corpus:
  words = doc.split()
  words_set = words_set.union(set(words))
# words_set.discard('') # This line is no longer needed after using split() without arguments
print('Number of words in the corpus:',len(words_set))
print('The words in the corpus: \n', words_set)
n_docs = len(corpus)
n_words_set = len(words_set)
df_tf = pd.DataFrame(np.zeros((n_docs, n_words_set)), columns=list(words_set))
# Compute Term  Frequency (TF)
for i in range(n_docs):
  words = [word for word in corpus[i].split() if word]
  for w in words:
    df_tf.loc[i, w] += 1/len(words) # Use .loc for clearer indexing
# Dataframe shows the frequency of each word in each document,
# a column for each word and a row for each document.
print("\nTerm Frequency (TF) DataFrame:")
print(df_tf) # Use display for better formatting
print("\nIDF of:")
idf = {}
for w in words_set:
  k = 0
  for i in range(n_docs):
    if w in corpus[i].split():
      k += 1
  if k > 0: # Avoid division by zero
    idf[w] = np.log10(n_docs/k)
    print(f'{w:>15}: {idf[w]:>10.4f}') # Format IDF to 4 decimal places
df_tf_idf = df_tf.copy()
for w in words_set:
  if w in idf: # Check if word exists in idf dictionary
    df_tf_idf[w] = df_tf[w] * idf[w]
print("\nTF-IDF DataFrame:")
print(df_tf_idf) # Use display for better formatting
