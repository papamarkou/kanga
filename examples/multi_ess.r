# Compute multivariate ESS using multiESS function of mcmcse package

## Load libraries

library(mcmcse)

## Read chains

chains <- read.table(file="chain01.csv", header=FALSE, sep=",")

## Compute multivariate ESS

print(multiESS(chains))

# print(multiESS(chains, covmat=mcse.multi(chains)$cov)) # Same as print(multiESS(chains))

print(multiESS(chains, covmat=mcse.initseq(chains)$cov))
