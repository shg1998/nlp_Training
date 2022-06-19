from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

tweet = """
The GRU illegal exposed earlier today by Dutch intelligence graduated from SAIS. I didn't have him in class as a student, but my amazing colleague Eugene Finkel did. Here's Eugene's courageous and remarkable thread on this experience
    Quote Tweet
    Eugene Finkel
    @eugene_finkel
    · Jun 16
    I had good reasons to hate Russian security services before. Now I am just exploding. I feel angry, I feel stupid, I feel naive, I feel tired. I got played. I had him in class. Twice, in fact. One class was half-Zoom  during COVID, several interactions outside classroom twitter.com/PjotrSauer/sta…
    Show this thread 
"""

# preprocess Tweet :

tweet_words = []

for word in tweet.split(' '):
    if(word.startswith('@') and len(word) > 1):
        word = "@user"
    elif word.startswith('http'):
        word = "http"
    tweet_words.append(word)

tweet_proc = " ".join(tweet_words)

# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

# sentiment analysis:
encoded_tweet = tokenizer(tweet_proc,return_tensors='pt')

output = model(**encoded_tweet)

scores = output[0][0].detach().numpy()
scores = softmax(scores)

for i in range(len(scores)):
    l = labels[i]
    s=scores[i]
    print(l,s)