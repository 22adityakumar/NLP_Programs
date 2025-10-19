#Stemming Algorithm

import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer , LancasterStemmer, SnowballStemmer

words=["running","Happiness","fishing","easily","studies","cries","nationality"]
porter=PorterStemmer()
lancaster=LancasterStemmer()
snowball=SnowballStemmer("english")

porter_stems=[porter.stem(w) for w in words]
lancaster_stems=[lancaster.stem(w) for w in words]
snowball_stems=[snowball.stem(w) for w in words]

print("Original -> Porter| Lancaster| Snowball \n")
for i,w in enumerate(words):
  print(f"{w:12} {porter_stems[i]:8} | {lancaster_stems[i]:9} | {snowball_stems[i]}")

fig,ax=plt.subplots(figsize=(16,5))

bar_width= 0.25
x=range(len(words))

ax.bar([i-bar_width for i in x],[len(s) for s in porter_stems],
       width=bar_width,label="Porter")
ax.bar(x,[len(s) for s in lancaster_stems],
       width=bar_width,label="Lancaster")
ax.bar([i+bar_width for i in x],[len(s) for s in snowball_stems],
       width=bar_width,label="Snowball")

ax.set_xticks([i for i in x])
ax.set_xticklabels(words,rotation=30)
ax.set_ylabel("Lenght of Stemmed Words")
ax.set_title("Comparison of Stemming Techniques")
ax.legend()

plt.tight_layout()
plt.show()
