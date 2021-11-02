Prediction Model
Arslan
18/03/2021

This model is very basic and just predicts based on the highest frequency but if we look at the predictions they are decently accurate and predicts many words correctly which will be depicted at the bottom section of this file.
I have just worked on a very basic note on this model and thus there are many ways the model can be optimised further by fitting a larger data and a more randomised approach, but intially this also works and works just fine for a basic level predictions.
The stored data was loaded from the RDS files :
library(tidyverse)
library(stringr)
bi_words <- readRDS("/Users/aashaysharma/Desktop/RStudio/DS-3/RDS/bi_words.rds")
tri_words <- readRDS("/Users/aashaysharma/Desktop/RStudio/DS-3/RDS/tri_words.rds")
quad_words <- readRDS("/Users/aashaysharma/Desktop/RStudio/DS-3/RDS/quad_words.rds")
Functions to get the most frequent NGrams :
#The function to get the most frequent bigrams
bigram <- function(input_words){
  num <- length(input_words)
  filter(bi_words, 
         word1==input_words[num]) %>% 
    top_n(1) %>%
    filter(row_number() == 1L) %>%
    select(num_range("word", 2)) %>%
    as.character() -> out
  ifelse(out =="character(0)", "?", return(out))
}

#The function to get the most frequent trigrams
trigram <- function(input_words){
  num <- length(input_words)
  filter(tri_words, 
         word1==input_words[num-1], 
         word2==input_words[num])  %>% 
    top_n(1) %>%
    filter(row_number() == 1L) %>%
    select(num_range("word", 3)) %>%
    as.character() -> out
  ifelse(out=="character(0)", bigram(input_words), return(out))
}

#The function to get the most frequent quadgrams
quadgram <- function(input_words){
  num <- length(input_words)
  filter(quad_words, 
         word1==input_words[num-2], 
         word2==input_words[num-1], 
         word3==input_words[num])  %>% 
    top_n(1) %>%
    filter(row_number() == 1L) %>%
    select(num_range("word", 4)) %>%
    as.character() -> out
  ifelse(out=="character(0)", trigram(input_words), return(out))
}
Ngrams prediction function which takes the input and formats it out in usable format for the functions.
predict <- function(input){
  # Create a dataframe
  input <- tibble(text = input)
  # Clean the Inpput
  replace_reg <- "[^[:alpha:][:space:]]*"
  input <- input %>%
    mutate(text = str_replace_all(text, replace_reg, ""))
  # Find word count, separate words, lower case
  input_count <- str_count(input, boundary("word"))
  input_words <- unlist(str_split(input, boundary("word")))
  input_words <- tolower(input_words)
  # Call the matching functions
  out <- ifelse(input_count == 1, bigram(input_words), 
                ifelse (input_count == 2, trigram(input_words), quadgram(input_words)))
  # Output
  return(out)
}
Predictions made by this logic:
predict("mothers")
## [1] "day"
predict("happy")
## [1] "birthday"
predict("barack")
## [1] "obama"
predict("This is united")
## [1] "states"
predict("This is united states of")
## [1] "america"
I would further work on the model for more accuracy and would update the same.
