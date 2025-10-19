import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

text = "How to remove stop words with NLTK Library in python"
print("Original Text:", text)

tokens = word_tokenize(text.lower())
print("Tokens:", tokens)

english_stopwords = stopwords.words('english')

tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]
tokens_stopwords_found = [t for t in tokens if t in english_stopwords]

print("Text without stop words:", " ".join(tokens_wo_stopwords))
print("Stop words found:", " ".join(tokens_stopwords_found))

english_stopwords.extend(['food', 'meal', 'eat'])
english_stopwords.append('plate')

if 'not' in english_stopwords:
  english_stopwords.remove('not')

print("\nCustomized English Stopwords Sample (first 30):")
print(english_stopwords[:30])

print("\nAvailable Languages in Stopwords Corpus:")
print(stopwords.fileids())

french_stopwords = stopwords.words('french')
spanish_stopwords = stopwords.words('spanish')
italian_stopwords = stopwords.words('italian')

print("\nFrench Stopwords Sample:", french_stopwords[:20])
print("Spanish Stopwords Sample:", spanish_stopwords[:20])
print("Italian Stopwords Sample:", italian_stopwords[:20])


from collections import Counter
import nltk
from nltk.corpus import stopwords
import re
import matplotlib.pyplot as plt

nltk.download("stopwords")
def top_non_stopwords_nltk(text,n=50):
  stop_words=set(stopwords.words('english'))
  words=re.findall(r'\w+',text.lower())
  filtered_words=[word for word in words if word not in stop_words]
  return Counter(filtered_words).most_common(n)

text="This is not a way to move a forward .This way is wrong,and we should not consider it.Moving forwards is the best way."
print(top_non_stopwords_nltk(text,10))
