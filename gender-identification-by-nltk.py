# importing libraries
import random
from nltk.corpus import names
import nltk
# nltk.download()


# Looking at the final name of the given name
#  Names ending in a, e, and i are likely to be female, while names ending in k, o, r, s, and t are likely to be male.
def gender_features(word):
    return {'last_letter': word[-1]}


# preparing a list of examples and corresponding class labels.
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])

random.shuffle(labeled_names)

# we use the feature extractor to process the names data.
featuresets = [(gender_features(n), gender)
               for (n, gender) in labeled_names]

# Divide the resulting list of feature
# sets into a training set and a test set.
train_set, test_set = featuresets[500:], featuresets[:500]

# The training set is used to
# train a new "naive Bayes" classifier.
classifier = nltk.NaiveBayesClassifier.train(train_set)

names = ["Adeline", "Arya", "Amalesh", "Aner", "Casta", "Hongjun", "Jani", "Magda", "Ritwik",  "Saima"]

for name in names:
    print(name + " - " + classifier.classify(gender_features(name)))

classifier.show_most_informative_features(10)
