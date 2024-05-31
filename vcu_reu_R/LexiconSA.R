install.packages("SentimentAnalysis")
install.packages("Snowballc")

library(SentimentAnalysis)
sentiment <- analyzeSearch("Yeah, this was a great soccer game of the German team!")
sentiment$SentimentQDAP
convertToBinaryResponse(sentiment)$SentimentGI
convertToDirection(sentiment$SentimentQDAP)

# Dictionaries
data(DictionaryHE)
str(DictionaryHE)

data(DictionaryLM)
str(DictionaryLM)

# Create a vector of strings:
documents <- c("Wow, I really like the new light sabers",
               "That book was excellent",
               "R is a great language",
               "The service in this restaurant was miserable",
               "This is neither positive nor negative",
               "The waiter forgot about my dessert -- what a poor service!")

# Extract dictionary-based sentiment according to QDAP Dictionary
sentiment$SentimentQDAP
# View sentiment direction 
convertToBinaryResponse(sentiment$SentimentQDAP)
convertToDirection(sentiment$SentimentQDAP)

# Customized dictionary
# Create a vector of strings
documents <- c("This is a very good thing!",
               "This is a good thing!",
               "This is an okay thing!",
               "This is a bad thing.",
               "This is a very bad thing!")
response <- c(1, 0.5, 0, -0.5, -1)

# Generate dictionary with LASSO regularization
dict <- generateDictionary(documents, resposne)

dict