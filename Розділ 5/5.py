#pip install nltk
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('rte')
from nltk import word_tokenize, sent_tokenize, RTEFeatureExtractor
from nltk.corpus import stopwords, rte
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn

print('Страп Андріана група 2 лаб 5')

def freq_table(text_string):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()
    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable

def score_sentence(sentences, freqTable):
    sent_value = dict()
    for sent in sentences:
        word_count_in_sentence = (len(word_tokenize(sent)))
        for wordValue in freqTable:
            if wordValue in sent.lower():
                if sent[:15] in sent_value:
                    sent_value[sent[:15]] += freqTable[wordValue]
                else:
                    sent_value[sent[:15]] = freqTable[wordValue]
        sent_value[sent[:15]] = sent_value[sent[:15]] / word_count_in_sentence
    return sent_value

def avg_score(sentValue):
    sumValues = 0
    for entry in sentValue:
        sumValues += sentValue[entry]
    avarage = sumValues / len(sentValue)
    return avarage

def summary(sentences, sentValue, threshold):
    sentence_count = 0
    summary = ''
    for sent in sentences:
        if sent[:15] in sentValue and sentValue[sent[:15]] > threshold:
            summary += " " + sent
            sentence_count += 1
    return summary

f = open('text.txt', 'r')
test_text = f.read()
fr=freq_table(test_text)
sen=sent_tokenize(test_text)
sv = score_sentence(sen, fr)
avg = avg_score(sv)
print('avg =', avg)
print(summary(sen, sv, avg))
print('------------------------------------------------')
print(summary(sen, sv, 3))

print('Логічні зв’язки (entailments) для першого значення дієслова win:', wn.synset('win.v.01').entailments())

rtepair = rte.pairs(['rte3_dev.xml'])[28]
extractor = RTEFeatureExtractor(rtepair)
print('Ключові слова з тексту:', extractor.text_words)
print('Ключові слова з гіпотези:', extractor.hyp_words) 
print('Перекриття між текстом і гіпотезою серед звичайних слів:', extractor.overlap('word'))
print('Перекриття між текстом і гіпотезою серед іменованих сутностей (NE):', extractor.overlap('ne'))
print('Звичайні слова, які містяться лише в гіпотезі:', extractor.hyp_extra('word'))
print('Іменовані сутності, які містяться лише в гіпотезі:', extractor.hyp_extra('ne'))
