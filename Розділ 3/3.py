#pip install nltk
import nltk
nltk.download('movie_reviews')
nltk.download('stopwords')
nltk.download('sentiwordnet')
from nltk.corpus import movie_reviews as mr
from random import shuffle
from nltk.corpus import stopwords
import string
from nltk.corpus import sentiwordnet as swn
from sklearn import linear_model
from nltk import NaiveBayesClassifier

print('Андріана Страп група 2 лаб 3')
all_words = nltk.FreqDist(mr.words())
shuffle(mr.fileids())
print(nltk.FreqDist(mr.words()).most_common(20))
print(nltk.FreqDist(mr.words())['marvelous'])

a = []
s = (mr.fileids('pos'))
for i in s:
    a.extend(mr.words(i))

b = []
d = (mr.fileids('neg'))
for i in d:
    b.extend(mr.words(i))

word = 'marvelous'
num1 = 0
num2 = 0
for i in a:
    if i == word:
        num1 += 1
for i in b:
    if i == word:
        num2 += 1
print(word, num1)
print(word, num2)

all_words = nltk.FreqDist(mr.words())
feature_vector = list(all_words)[:4900]

def find_feature(word_list):
    feature = {}
    for x in feature_vector:
        feature[x] = x in word_list
    return feature

print(find_feature(mr.words('pos/cv028_26746.txt')))

def extract_features(word_list):
    return dict([(word, True) for word in word_list])

positive_fileids = mr.fileids('pos')
negative_fileids = mr.fileids('neg')
features_positive = [(extract_features(mr.words(fileids=[f])), 'Positive') for f in positive_fileids]
features_negative = [(extract_features(mr.words(fileids=[f])), 'Negative') for f in negative_fileids]

threshold_factor = 0.9
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))

features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:] + features_negative[threshold_negative:]

classifier = NaiveBayesClassifier.train(features_train)
classifier.show_most_informative_features(20)
print("Accuracy of the classifier:", nltk.classify.util.accuracy(classifier, features_test))

stop = list(set(stopwords.words('english')))
documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]
shuffle(documents)

training_data = documents[:1500]
testing_data = documents[1500:]
vocabulary = []
for i in range(0, len(training_data)):
    vocabulary.extend(training_data[i][0])
vocabulary = list(set(vocabulary))
vocabulary.sort()

def get_senti_wordnet_features(data):
    fet_vec_all = []
    for tup in data:
        words = tup[0]
        pos_score = 0
        neg_score = 0
        for w in words:
            senti_synsets = swn.senti_synsets(w.lower())
            for senti_synset in senti_synsets:
                p = senti_synset.pos_score()
                n = senti_synset.neg_score()
                pos_score += p
                neg_score += n
                break
        fet_vec_all.append([float(pos_score), float(neg_score)])
    return fet_vec_all

def get_unigram_features(data, vocab):
    fet_vec_all = []
    for tup in data:
        single_feat_vec = []
        words = tup[0]
        for v in vocab:
            if v in words:
                single_feat_vec.append(1)
            else:
                single_feat_vec.append(0)
        fet_vec_all.append(single_feat_vec)
    return fet_vec_all

def merge_features(featureList1, featureList2):
    if featureList1 == []:
        return featureList2
    merged = []
    for i in range(len(featureList1)):
        m = featureList1[i] + featureList2[i]
        merged.append(m)
    return merged

def get_labels(data):
    labels = []
    for tup in data:
        if tup[1].lower() == "neg":
            labels.append(-1)
        else:
            labels.append(1)
    return labels

def calculate_precision(prediction, actual):
    prediction = list(prediction)
    correct_labels = [prediction[i] for i in range(len(prediction)) if actual[i] == prediction[i]]
    precision = float(len(correct_labels)) / float(len(prediction))
    return precision

training_unigram_features = get_unigram_features(training_data, vocabulary)
training_swn_features = get_senti_wordnet_features(training_data)
training_features = merge_features(training_unigram_features, training_swn_features)
training_labels = get_labels(training_data)

test_unigram_features = get_unigram_features(testing_data, vocabulary)
test_swn_features = get_senti_wordnet_features(testing_data)
test_features = merge_features(test_unigram_features, test_swn_features)
test_gold_labels = get_labels(testing_data)

Logreg = linear_model.LogisticRegression(C=1e5)
LogClassifier = Logreg.fit(training_features, training_labels)
predictions = LogClassifier.predict(training_features)
print("Precision of linear Logistic Regression is:")
precision = calculate_precision(predictions, training_labels)
print("Training data\t" + str(precision))
predictions = LogClassifier.predict(test_features)
precision = calculate_precision(predictions, test_gold_labels)
print("Test data\t" + str(precision))