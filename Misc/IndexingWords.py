
# coding: utf-8

#Create an index of what pages words appear on given a text

data = "The Project Gutenberg EBook of Adventures of Huckleberry Finn, Complete by Mark Twain (Samuel Clemens) This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.net Title: Adventures of Huckleberry Finn, Complete Author: Mark Twain (Samuel Clemens) Release Date: August 20, 2006 [EBook #76] Last Updated: April 18, 2015] Language: English Character set encoding: ISO-8859-1 *** START OF THIS PROJECT GUTENBERG EBOOK HUCKLEBERRY FINN *** Produced by David Widger ADVENTURES OF HUCKLEBERRY FINN (Tom Sawyer's Comrade) By Mark Twain Complete CONTENTS. CHAPTER I. Civilizing Huck.--Miss Watson.--Tom Sawyer Waits. CHAPTER II. The Boys Escape Jim.--Torn Sawyer's Gang.--Deep-laid Plans. CHAPTER III. A Good Going-over.--Grace Triumphant.--"


data = data.replace(',','')
data = data.replace('.','')
data = data.replace('(','')
data = data.replace(')','')
data = data.replace('-','')
data = data.replace('*','')
datasplit = data.split(' ')

from collections import defaultdict
from collections import OrderedDict
import math
import re
from time import time
import sys

t0 = time()


words = re.findall(r'\w+', open(sys.argv[1]).read().lower())
wordsPerPage = sys.argv[3]
dictionary = defaultdict(list)
count = 0
for word in words:
    startchar = count
    endchar = count + len(word)
    startpage = math.floor(startchar/wordsPerPage)
    endpage = math.floor(endchar/wordsPerPage)
    if(startpage == endpage):
        page = (startpage+1)
    else:
        page = (endpage+1)
    count = endchar
    if word not in dictionary or page not in dictionary[word]:
        dictionary[word].append(page)
sortedDict = OrderedDict(sorted(dictionary.items()))
with open(sys.argv[2], 'w') as f:
    f.writelines('{} {} \n'.format(k,v) for k, v in sortedDict.items())
t1 = time()
print((t1-t0)*1000)

