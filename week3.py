import nltk
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics.association import BigramAssocMeasures, TrigramAssocMeasures
from nltk.corpus import stopwords
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = """
natural language processing is a fascinating
area of artificial intelligence.
it deals with how computers understand
and generate human language. 
word collocation are pair of words that
appear together more often than by chance.
for example, 'artificial intelligence',
'machine learning', and 'deep learning'.
"""

# Tokenize and preprocess text
tokens = nltk.word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
filtered_tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]

# Bigrams
print('\n=== TOP BIGRAM COLLOCATIONS (with PMI scores) ===')
bigram_finder = BigramCollocationFinder.from_words(filtered_tokens)
bigram_finder.apply_freq_filter(1)
scored_bigrams = bigram_finder.score_ngrams(BigramAssocMeasures.pmi)

for (w1, w2), score in scored_bigrams[:10]:
  print(f"{w1}-{w2} | PMI: {score:.4f}")

# Trigrams
print('\n=== TOP TRIGRAM COLLOCATIONS (with PMI scores) ===')
trigram_finder = TrigramCollocationFinder.from_words(filtered_tokens)
trigram_finder.apply_freq_filter(1)
scored_trigrams = trigram_finder.score_ngrams(TrigramAssocMeasures.pmi)

for (w1, w2, w3), score in scored_trigrams[:10]:
  print(f"{w1}-{w2}-{w3} | PMI: {score:.4f}")

# b. Program to print all words beginning with a given sequence of letters

# Sample text or list of words
text = """Natural language processing is a fascinating area of
artificial intelligence. It deals with how computers understand
and generate human language."""

# Convert text to a list of words
words = text.split()

# Ask user for the sequence of letters
prefix = input("Enter the starting sequence: ").lower()

# Print words beginning with the given prefix
print(f"\nWords beginning with '{prefix}':")
for word in words:
    clean_word = word.strip('.,!;:').lower()
    if clean_word.startswith(prefix):
        print(clean_word)


# c.
# Sample text
text = "natural language processing is a fascinating area of artificial intelligence"

# Split the text into words
words = text.split()

# Print words longer than 4 characters
print("Words longer than 4 characters:")
for word in words:
    clean_word = word.strip('.,!?;:')
    if len(clean_word) > 4:
        print(clean_word)
