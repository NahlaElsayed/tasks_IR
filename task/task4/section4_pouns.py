import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Open CSV file
with open('top 100 streamed songs.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Create a list of all words in the CSV file
    words = []
    for row in reader:
        for word in row:
            words.append(word)

    # Tokenize the words
    tokens = nltk.word_tokenize(''.join(words))

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if not word.lower() in stop_words]

    # Stem the tokens
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
print(filtered_tokens)
#print(stemmed_tokens)