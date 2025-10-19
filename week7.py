import nltk
from collections import defaultdict, Counter
from nltk.util import ngrams,bigrams
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Step 1: Input Paragraph
text = """ Your current feeling that your knowledge isn't useful might be because you're in an environment that doesn't value your specific skills.
There are countless fields—in data science, software engineering, research, logistics, and analytics—where your pattern-recognition ability is incredibly useful and highly valued,
often with less emphasis on constant high-stakes social interaction."""

print("=== INPUT PARAGRAPH ===")
print(text)

# Step 2: Tokenization and POS Tagging

words = word_tokenize(text)
pos_tags = nltk.pos_tag(words, tagset='universal')

print("\n=== (a) POS TAGGING ===")
print("Each word is assigned a grammatical tag:\n")
print(len(pos_tags))

# Step 3: Word with Greatest Number of Distinct Tags
word_tags = defaultdict(set)
for word, tag in pos_tags:
  word_tags[word].add(tag)

word_with_most_tags = max(word_tags.items(), key=lambda x: len(x[1]))

print("\n=== (b) WORD WITH GREATEST NUMBER OF DISTINCT TAGS ===")
print(f"Word: {word_with_most_tags[0]}")
print(f"Tags: {word_with_most_tags[1]}")
print("This word is used in different in different roles.")

#Step 4: Tags in Decreasing Frequency
all_tags = [tag for _, tag in pos_tags]
tag_frequency = Counter(all_tags)

print("\n=== (c) TAGS IN DECREASING FREQUENCY ===")
print("Tags Sorted by decreasing frequency:\n")
for tag, frequency in tag_frequency.most_common():
  print(f"{tag:5} -> {frequency}")

print("\nCommon tags:")
tag_meanings = {
'NOUN': 'Noun(person, place, thing, idea)',
'VERB': 'Verb(action or state)',
'ADJ': 'Adjective(describes a noun)',
'ADV': 'Adverb(describes a verb/adjective)',
'ADP': 'Adposition(prepositions and postpositions)',
'CONJ': 'Conjunction(coordinating conjunctions)',
'DET': 'Determiner(articles, pronouns, etc.)',
'NUM': 'Numeral(one, two, etc.)',
'PRT': 'Particle(prepositions, articles, etc.)',
'PRON': 'Pronoun(he, she, they)',
'X': 'Other(unknown)',

}

# Step 5: Most Common Tags After a Noun
tagged_bigrams = list(bigrams(pos_tags))
after_noun = Counter(tag for (word, tag), (next_word, next_tag) in tagged_bigrams if tag == 'NOUN')

print("\n=== (d) MOST COMMON TAGS AFTER A NOUN ===")
for tag, frequency in after_noun.most_common():
  print(f"{tag:5} -> {frequency}")

print("- VERB after NOUN")
print("- ADJ after NOUN")
print("- ADV after NOUN")
print("- DET after NOUN")
print("- NUM after NOUN")
print("- PRT after NOUN")
print("- PRON after NOUN")
print("- Another NOUN : compound nouns")
