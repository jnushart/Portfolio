
# coding: utf-8

# In[4]:


#Utilizes scraping and matplot to print out the frequency of words in Moby Dick

import requests
from bs4 import BeautifulSoup
import nltk

r = requests.get('https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm')

# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extracting the HTML from the request object
html = r.text

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, 'html.parser')

# Getting the text out of the soup
text = soup.get_text()

# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

# Tokenizing the text
tokens = tokenizer.tokenize(text)

words = []

# Looping through the tokens and make them lower case
for word in tokens:
    words.append(word.lower())

get_ipython().run_line_magic('matplotlib', 'inline')

# Creating the word frequency distribution
freqdist = nltk.FreqDist(words)

# Plotting the word frequency distribution
freqdist.plot(25)

