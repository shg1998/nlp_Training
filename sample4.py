import os
import nltk
import nltk.corpus
from nltk.corpus import brown, stopwords
from nltk.tokenize import word_tokenize, blankline_tokenize
from nltk.probability import FreqDist
from nltk.util import bigrams, trigrams, ngrams
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, wordnet, WordNetLemmatizer
from nltk import ne_chunk
import re 


# print(os.listdir(nltk.data.find("corpora")))
# print(brown.words())
# print(nltk.corpus.gutenberg.fileids())
hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
# print(hamlet)
# for word in hamlet[:500]:
#     print(word,sep= ' ',end=' ')

text = """
The GRU illegal exposed earlier today by Dutch intelligence graduated from SAIS. I didn't have him in class as a student, but my amazing colleague Eugene Finkel did. Here's Eugene's courageous and remarkable thread on this experience
    Quote Tweet
    Eugene Finkel
    @eugene_finkel
    · Jun 16
    I had good reasons to hate Russian security services before. Now I am just exploding. I feel angry, I feel stupid, I feel naive, I feel tired. I got played. I had him in class. Twice, in fact. One class was half-Zoom  during COVID, several interactions outside classroom twitter.com/PjotrSauer/sta…
    Show this thread """

text_tokens = word_tokenize(text)
fdist = FreqDist()

# find repeatance of each words in sentence (frequency):
for word in text_tokens:
    fdist[word.lower()] += 1

# distinct words numbers :)
# print(len(fdist))

fdist_top10 = fdist.most_common(10)
# print(fdist_top10)

text_blank = blankline_tokenize(text)
# print(len(text_blank))


text_bigrams = list(nltk.bigrams(text_tokens))
# print(text_bigrams)

text_trigrams = list(nltk.trigrams(text_tokens))
# print(text_trigrams)

text_ngrams = list(nltk.ngrams(text_tokens, 5))
# print(text_ngrams)

# find root of words
pst = PorterStemmer()
# print(pst.stem("hading"))

lst = LancasterStemmer()
# print(lst.stem("having"))

sst = SnowballStemmer('english')
# print(sst.stem("fading"))

# nltk.download('omw-1.4')
# word_lem = WordNetLemmatizer()
# print(word_lem.lemmatize('corpora'))

# nltk.download('stopwords')
# print(stopwords.words('english'))

# remove all extra words:)
punctuation = re.compile(r'[-.?!,:;()|0-9]')
post_punctuation = []
for words in text_tokens:
    word = punctuation.sub("",words)
    if len(word) > 0:
        post_punctuation.append(word)

# for token in text_tokens:
#     print(nltk.pos_tag([token]))

# text_tags = nltk.pos_tag(word_tokenize(text))
# text_NER = ne_chunk(text_tags)
# print(text_NER)