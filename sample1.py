import re
from turtle import color
from matplotlib import pyplot as plt
import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
from utils.data import RawData


df = pd.DataFrame(RawData.get_data(), columns=["Tweets"])


def clean_txt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # Removes @mentions
    text = re.sub(r'#', '', text)  # Removing the '#' symbol
    text = re.sub(r'RT[\s]+', '', text)  # Removing RT
    text = re.sub(r'https?:\/\/\S+', '', text)  # Removing the hyper link
    return text


df['Tweets'] = df['Tweets'].apply(clean_txt)

# print(df.head())

# create a function to get the subjectivity :


def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

 # create a function to get the polarity:


def get_polarity(text):
    return TextBlob(text).sentiment.polarity


# create two new columns:
df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] = df['Tweets'].apply(get_polarity)

# show new Dataframe with the new columns
# print(df)


# plot Word Cloud

allWords = ' '.join([twts for twts in df['Tweets']])
wordCloud = WordCloud(width=500, height=300, random_state=21,
                      max_font_size=119).generate(allWords)
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
# plt.show()

# create a function  to compute the negative , neutral and positive analysis


def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


df['Analysis'] = df['Polarity'].apply(getAnalysis)

# show the dataframe
# print(df)

# print all of the positive tweets:
print("✔✔✔✔✔✔✔✔✔✔✔✔Positive✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
j = 1
sortedDf = df.sort_values(by=['Polarity'])
for i in range(0, sortedDf.shape[0]):
    if(sortedDf['Analysis'][i] == 'Positive'):
        print(str(j) + ") " + str(sortedDf['Tweets'][i]))
        j += 1
        print("//////////////////////////////////////////////")


print("✔✔✔✔✔✔✔✔✔✔✔✔Negative✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
# print all of the negative tweets:
k = 1
sortedDf2 = df.sort_values(by=['Polarity'])
for i in range(0, sortedDf2.shape[0]):
    if(sortedDf2['Analysis'][i] == 'Negative'):
        print(str(k) + ") " + str(sortedDf2['Tweets'][i]))
        k += 1
        print("//////////////////////////////////////////////")

print("✔✔✔✔✔✔✔✔✔✔✔✔Neutral✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")


h = 1
sortedDf3 = df.sort_values(by=['Polarity'])
for i in range(0, sortedDf3.shape[0]):
    if(sortedDf3['Analysis'][i] == 'Neutral'):
        print(str(h) + ") " + str(sortedDf3['Tweets'][i]))
        h += 1
        print("//////////////////////////////////////////////")

plt.figure(figsize=(8, 6))
for i in range(0, df.shape[0]):
    plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')
plt.title('sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()

# get the percentage of positive tweets
ptweets = df[df.Analysis == 'Positive']
ptweets = ptweets['Tweets']

print("positive Tweets Percantage : " + str(round((ptweets.shape[0] / df.shape[0]) * 100, 1)))


# plot and visualize the counts as column chart :)
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind='bar')
plt.show()