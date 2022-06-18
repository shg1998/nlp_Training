import re
import pandas as pd
from textblob import TextBlob

tweets = [
    'My daughter went to a laser quest birthday party yesterday. She set her username to “a girl”. I asked why she didn’t pick bloodstone’ ',
    'CRO at @WithSecure. Infosec speaker and author. My book "If Its Smart, Its Vulnerable" is coming out in August. I stand with Ukraine.',
    'Red Line Through HTTPS http://xkcd.com/2634',
    'What kind of ratings is the Apple ’Phone’ app getting in your App Store? If the Finnish App Store it gets 4.2 out of 5.',
    'Amazing indeed!']
df = pd.DataFrame(tweets, columns=["Tweets"])




def clean_txt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # Removes @mentions
    text = re.sub(r'#', '', text)  # Removing the '#' symbol
    text = re.sub(r'RT[\s]+', '', text) # Removing RT
    text = re.sub(r'https?:\/\/\S+', '', text) # Removing the hyper link
    return text

df['Tweets'] = df['Tweets'].apply(clean_txt)

# print(df.head())

# create a function to get the subjectivity : 
def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity


 # create a function to get the polarity:
def  get_polarity(text):
    return TextBlob(text).sentiment.polarity

# create two new columns:
df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] = df['Tweets'].apply(get_polarity)

# show new Dataframe with the new columns
print(df.head())
