install.packages("text2vec")
install.packages("ROCR")
library(text2vec)
library(ROCR)
library(ggplot2)

data("movie_review")
# Clean up the review
movie_review$review <- 