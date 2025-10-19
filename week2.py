# Pre-Defined
from nltk.util import ngrams

# Example Sentence
text = """Education empowers students to learn and education
helps teachers to guide and education creates
opportunities to learn and grow in education system around
the world."""

# Tokenize the text into words
words = text.split()

# Create n-grams and store them as lists so they can be reused
unigrams = list(ngrams(words, 1))
bigrams = list(ngrams(words, 2))
trigrams = list(ngrams(words, 3))
quadgrams = list(ngrams(words, 4))

# Print all n-grams
print("=== UNIGRAMS ===")
for gram in unigrams:
  print(gram)

print("\n=== BIGRAMS ===")
for gram in bigrams:
  print(gram)

print("\n=== TRIGRAMS ===")
for gram in trigrams:
  print(gram)

print("\n=== 4-GRAMS ===")
for gram in quadgrams:
  print(gram)

from collections import defaultdict

def highest_probability(text):
  words= text.split()
  bigram_counts=defaultdict(lambda:defaultdict(int))
  first_word_counts = defaultdict(int)
  
  for i in range(len(words)-1):
    w1=words[i]
    w2 = words[i + 1]
    bigram_counts[w1][w2]+=1
    first_word_counts[w1]+=1
  result={}
  for w1 in bigram_counts:
    max_prob = 0
    best_w2=None
    for w2 in bigram_counts[w1]:
      prob=bigram_counts[w1][w2]/first_word_counts[w1]
      if prob > max_prob:
        max_prob=prob
        best_w2 = w2
    result[w1]=(best_w2,max_prob)
  return result

text = "Education empowers to learn and education helps teachers to guide and education creates opportunities to learn and grow in educational systems around the world."

output=highest_probability(text)
print("Highest probability of a word(w2)occurring after another word(w1):")
for w1, (w2,prob) in output.items():
  print(f"After'{w1}'->'{w2}' with probability{prob:.2f}")


