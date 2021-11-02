Introduction
This is DataScience Capstone Project from JHU associated with Swift key. It is a NLP project where we need to work with a basic real life data, transform it into useful form, cleaning it and run some exploratory tests to solidify our model apporach. After all steps we need to develop a model which can be used to predict the next word on the basis of provided word by user.
This is the first Milestone file where we accomplish Task 1 and 2 that is, cleaning the data and running some exploratory tests and plotting some graphs to gain some insight on the data.
Loading the data :
Recquired Libraries :

library(ggplot2)
library(tm)
library(tmap)
library(dplyr)
library(wordcloud)
library(gridExtra)
news <- readLines("/Users/aashaysharma/Desktop/RStudio/DS-Capstone/final/en_US/en_US.news.txt")

blogs <- readLines("/Users/aashaysharma/Desktop/RStudio/DS-Capstone/final/en_US/en_US.blogs.txt")

twitter2 <- readLines("/Users/aashaysharma/Desktop/RStudio/DS-Capstone/final/en_US/en_US.twitter.txt")
Generating some random sample from the data as the data is too big and our vector memory is limited we will use a small sample to work with.

random_twitter2 <- ceiling(runif(n=6000, min=0, max=length(twitter2)))
random_news <- ceiling(runif(n=5000, min=0, max=length(news)))
random_blogs <- ceiling(runif(n=5000, min=0, max=length(blogs)))

twitter2 <- twitter2[random_twitter2]
blogs <- blogs[random_blogs]
news <- news[random_news]
Converting the encoding of the random sample to UTF-8 so that our tokenizers can easily work on the data without any logical error.

twitter2 <- iconv(twitter2, "UTF-8", "ASCII", sub="")
news <- iconv(news, "UTF-8", "ASCII", sub="")
blogs <- iconv(blogs, "UTF-8", "ASCII", sub="")
Now creating a VCorpus by combining all the data of the three random samples so that we can use RWeka's N gram Tokenizer to tokenize the text into 1,2 and 3 grams, addtionally we are also cleaning the corpus using some built in functions we are :

Removing Numbers
Removing Punctuations
Converting to lowercase
Removing Profanity
and separately removing stop words
and removing badwords
myCorpus <- VCorpus(VectorSource(c(twitter2, blogs, news)))
myCorpus <- tm_map(myCorpus, removeNumbers)
myCorpus <- tm_map(myCorpus, removePunctuation)
myCorpus <- tm_map(myCorpus, content_transformer(tolower))
myCorpus <- tm_map(myCorpus, stripWhitespace)
I have already preprocessed a file for badwords (Google's Badwords file) and loaded it into RStudio

badwords <- readLines("/Users/aashaysharma/Desktop/badwords.txt")
badwords <- removePunctuation(badwords)
badwords <- removeNumbers(badwords)
myCorpus_nostop <- tm_map(myCorpus, removeWords, stopwords("en"))

myCorpus <- tm_map(myCorpus, removeWords, badwords)
myCorpus_nostop <- tm_map(myCorpus_nostop, removeWords, badwords)
Tokenizing
Now that we have finally cleaned up our Corpus now we can initialize a Uni,Bi and Tri gram tokenizer to tokenize our data into words. We will do this for both the data containing and not containing the english stop words so that we can gain so insights that how the data looks and what are the frequencies in both the cases.

unigram <- function(x) {RWeka::NGramTokenizer(x, RWeka::Weka_control(min = 1, max = 1))}
bigram <- function(x) {RWeka::NGramTokenizer(x, RWeka::Weka_control(min = 2, max = 2))}
trigram <- function(x) {RWeka::NGramTokenizer(x, RWeka::Weka_control(min = 3, max = 3))}
Converting our data into a termDocumentMatrix after tokenizing:

tdmUnigram <- TermDocumentMatrix(myCorpus, control = list(tokenize = unigram))
tdmBigram <- TermDocumentMatrix(myCorpus, control = list(tokenize = bigram))
tdmTrigram <- TermDocumentMatrix(myCorpus, control = list(tokenize = trigram))


#For data set containing no stop words
tdmUnigram_no <- TermDocumentMatrix(myCorpus_nostop, control = list(tokenize = unigram))
tdmBigram_no <- TermDocumentMatrix(myCorpus_nostop, control = list(tokenize = bigram))
tdmTrigram_no <- TermDocumentMatrix(myCorpus_nostop, control = list(tokenize = trigram))
Geeting the frequency of the tokenized words:

unigramFreq <- sort(rowSums(as.matrix(tdmUnigram)), decreasing = T)
bigramFreq <- sort(rowSums(as.matrix(tdmBigram)), decreasing = T)
trigramFreq <- sort(rowSums(as.matrix(tdmTrigram)), decreasing = T)

#for dataset containing no stop words:

unigramFreq_no <- sort(rowSums(as.matrix(tdmUnigram_no)), decreasing = T)
bigramFreq_no <- sort(rowSums(as.matrix(tdmBigram_no)), decreasing = T)
trigramFreq_no <- sort(rowSums(as.matrix(tdmTrigram_no)), decreasing = T)
Just arranging the data and getting our top 20 in all the cases and performing some plots
The Plot for frequencies containing the stop words:

![unnamed-chunk-12-1](https://user-images.githubusercontent.com/45125597/111650158-12bd8380-8816-11eb-894b-f55fc94814bd.png)


The Plot for frquencies not containing the stop words:
![unnamed-chunk-13-1](https://user-images.githubusercontent.com/45125597/111650260-2cf76180-8816-11eb-8e40-494aec3c2207.png)


Plotting the word clouds :
WordCloud for the corpus containing stop words:
UNIGRAM
![unnamed-chunk-14-1](https://user-images.githubusercontent.com/45125597/111650377-49939980-8816-11eb-8e46-aaa80f0e82dd.png)


BIGRAM

![unnamed-chunk-15-1](https://user-images.githubusercontent.com/45125597/111650436-57e1b580-8816-11eb-8620-5c2e2ea45d11.png)

TRIGRAM
![unnamed-chunk-16-1](https://user-images.githubusercontent.com/45125597/111650510-6c25b280-8816-11eb-9b65-301d045d8591.png)


WordCloud for the corpus NOT containing stop words:
UNIGRAM
![unnamed-chunk-17-1](https://user-images.githubusercontent.com/45125597/111650598-7fd11900-8816-11eb-9367-cb6785fa467c.png)


BIGRAM
![unnamed-chunk-18-1](https://user-images.githubusercontent.com/45125597/111650697-98413380-8816-11eb-9e2c-4777fe9e1f24.png)


TRIGRAM
![unnamed-chunk-19-1](https://user-images.githubusercontent.com/45125597/111650816-b73fc580-8816-11eb-8218-70a920fb04f2.png)

