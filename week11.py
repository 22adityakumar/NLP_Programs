import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.tree import Tree

# Text
text = "The quick brown fox jumps over the lazy dog near the river bank"

# Tokenize and POS tagging
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

print("POS Tagged Sentence:\n", pos_tags)
print("-" * 80)

# ---------------- CHUNKING ----------------
chunk_grammar = r"""NP: {<DT>?<JJ>*<NN.*>+}"""
chunk_parser = RegexpParser(chunk_grammar)
chunk_tree = chunk_parser.parse(pos_tags)

print("Chunking Result (Noun Phrases):")
for subtree in chunk_tree.subtrees():
    if subtree.label() == 'NP':
        print(" ".join(word for word, tag in subtree.leaves()))

print("-" * 80)

# ---------------- CHINKING ----------------
chink_grammar = r"""
NP:
    {<DT>?<JJ>*<NN.*>+}   # First chunk NPs
    }<VB.*|IN>+{          # Then chink verbs and prepositions
"""

chink_parser = RegexpParser(chink_grammar)
chink_tree = chink_parser.parse(pos_tags)

print("Chinking Result (After Removing Verbs & Prepositions):")
for subtree in chink_tree.subtrees():
    if subtree.label() == 'NP':
        print(" ".join(word for word, tag in subtree.leaves()))

print("-" * 80)

print("Chunk Tree Structure:\n")
print(chunk_tree.pformat(margin=70))
print("-" * 80)

print("Chink Tree Structure:\n")
print(chink_tree.pformat(margin=70))
