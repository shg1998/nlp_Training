from nrclex import NRCLex
import numpy as np
import pandas as pd

#Assign Emotion
text = "Your website is perfect 😊"

#create object
emotion = NRCLex(text)

#using methods to classify emotion
print('\n',emotion.words)
print('\n',emotion.affect_dict)