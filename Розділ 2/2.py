#pip install nltk
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from operator import itemgetter
import re
print('Андріана Страп група 2 лаб2')
n1 = 'pineapple'
n2 = 'apple'
noun1 = wn.synsets(n1)[0]
noun2 = wn.synsets(n2)[0]
print(noun1.definition())
print(noun2.definition())
print(noun1.hypernyms())
print(noun2.hypernyms())
print(noun1.hyponyms())
print(noun2.hyponyms())
print(noun1.lowest_common_hypernyms(noun2))
print(noun1.path_similarity(noun2))
print(noun1.wup_similarity(noun2))
print(noun1.lch_similarity(noun2))
def levenshtein(s1,s2):
    n = range(0,len(s1)+1)
    for y in range(1,len(s2)+1):
        l,n = n,[y]
        for x in range(1,len(s1)+1):
            n.append(min(l[x]+1,n[-1]+1,l[x-1]+((s2[y-1]!=s1[x-1]) and 1 or 0)))
    return n[-1]
def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                           )
    if i and j and s1[i] == s2[j-1] and s1[i-1] == s2[j]:
        d[(i,j)] = min(d[(i,j)], d[i-2,j-2] + 1) # transposition
    return d[lenstr1-1,lenstr2-1]
print(levenshtein(n1, n2))
print(damerau_levenshtein_distance(n1, n2))
def dict_distance(text, word, num_words):
    file = open(text, 'r')
    lines = file.readlines()
    file.close()
    distances = {}
    for line in lines:
        word_distance = levenshtein(word,line.strip())
        distances[line.strip()] = word_distance
    sorted_dict = sorted(distances.items(), key = itemgetter(1))
    closest_words = []
    for i in range(num_words):
        closest_words.append(sorted_dict[i])
    return closest_words
word = 'cat'
text = '1-1000.txt'
print(word, ": ", dict_distance(text, word, 8))
frequency = {}
document_text = open('melville-moby_dick.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,25}\b', text_string)
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count = most_frequent.keys()
with open("words.txt", "w") as file:
    file.write(("\n".join("{}".format(p) for p in most_frequent_count)))
word = 'break'
print(word, ": ", dict_distance("words.txt", word, 4))
