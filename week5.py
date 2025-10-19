import nltk
from nltk.corpus import wordnet

# Download required data
nltk.download('wordnet')
nltk.download('omw-1.4')

# ---------------- SYNONYMS & ANTONYMS ----------------
def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                for ant in lemma.antonyms():
                    antonyms.add(ant.name())
    return synonyms, antonyms

word = "sofa"
synonyms, antonyms = get_synonyms_antonyms(word)

print(f"Word: {word}")
print("\nSynonyms:")
print(", ".join(sorted(synonyms)) if synonyms else "None Found")

print("\nAntonyms:")
print(", ".join(sorted(antonyms)) if antonyms else "None Found")

# ---------------- HYPONYMS, POLYSEMY & HOMONYMS ----------------
def get_hyponyms(word):
    hyponyms = set()
    for syn in wordnet.synsets(word):
        for hypo in syn.hyponyms():
            for lemma in hypo.lemmas():
                hyponyms.add(lemma.name())
    return sorted(hyponyms)

def get_polysemy(word):
    senses = wordnet.synsets(word)
    return senses if senses else []

def get_homonyms(word):
    homonyms = set()
    original_senses = wordnet.synsets(word)
    for syn in original_senses:
        for lemma in syn.lemmas():
            if lemma.name() != word:
                other_senses = wordnet.synsets(lemma.name())
                for osyn in other_senses:
                    if osyn.name().split('.')[0] == lemma.name() and osyn not in original_senses:
                        homonyms.add(lemma.name())
    return sorted(homonyms)

def display_word_relations(word):
    print(f"\nWord: {word}")
    print("-" * 40)

    # Hyponyms
    hypos = get_hyponyms(word)
    print("\nHyponyms (More specific types):")
    print(", ".join(hypos) if hypos else "No hyponyms found.")

    # Polysemy
    senses = get_polysemy(word)
    print(f"\nPolysemy (Number of meanings): {len(senses)}")
    for i, sense in enumerate(senses, 1):
        print(f"  {i}. {sense.definition()}")

    # Homonyms
    homs = get_homonyms(word)
    print("\nHomonyms (Same word, different meanings):")
    print(", ".join(homs) if homs else "No homonyms found.")

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    word = input("\nEnter a word: ").strip().lower()
    display_word_relations(word)
