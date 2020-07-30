# Compute initial sequence variance estimator using initseq function of mcmc package

## Load libraries

library(mcmc)

## Read chains

chains <- read.table(file="chain01.csv", header=FALSE, sep=",")

## Compute correlation matrix

print(cor(chains))
