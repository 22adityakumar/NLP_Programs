import nltk
from nltk.tokenize import word_tokenize

# NLTK needs this package for tokenization
nltk.download('punkt')

# The text we want to analyze
text = """
Natural Language Processing is an exciting field of Artificial Intelligence. It allows computers to understand, interpret, and generate human language. 
This field includes tasks such as speech recognition, machine translation, and text summarization.
"""

# Split the text into a list of words
word_tokens = word_tokenize(text)

# --- Using a simple for loop to clean the words ---
cleaned_words = []  # Start with an empty list
for word in word_tokens:
    # Check if the token consists only of letters
    if word.isalpha():
        # If yes, convert it to lowercase and add it to our list
        cleaned_words.append(word.lower())

# Now, we can analyze our cleaned list
total_words = len(cleaned_words)
distinct_words = len(set(cleaned_words))

# Print the results
print("--- Word Analysis ---")
print("Total number of words:", total_words)
print("Number of distinct words:", distinct_words)
print("\nDistinct Words List:", sorted(set(cleaned_words)))