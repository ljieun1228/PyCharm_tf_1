from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
from nltk import FreqDist

import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt #그림그래프

#re=> 정규식
#'r'=> read only

okt = Okt()
ctx = '../data/'
filename = ctx+'kr-Report_2018.txt'
stopword = ctx+'stopwords.txt'

with open(filename,'r',encoding='utf-8') as f :
    texts = f.read()

texts = texts.replace('\n','')
tokenizer = re.compile(r'[^ ㄱ-힣]+')
#^부정 한글, 띄어쓰기 제외한 모든 글자 제거
texts = tokenizer.sub('', texts)

tokens = word_tokenize(texts)

noun_tokens = []
for t in tokens:
    t_pos = okt.pos(t)
    t2 = [i[0] for i in t_pos
          if i[1]=='Noun']
    if len("".join(t2)) > 1:
        noun_tokens.append("".join(t2))

texts = " ".join(noun_tokens)

with open(stopword,'r',encoding='utf-8') as f:
    stopwords = f.read()

stopwords = stopwords.split(' ')
texts = [text for text in tokens if text not in stopwords]
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)

okt.pos('가치창출')
okt.pos('갤럭시')
#이 단어들은 살려라

wcloud = WordCloud(ctx+'D2Coding.ttf'
                   ,relative_scaling=0.2
                   ,background_color='pink').generate(" ".join(texts))

plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.show()