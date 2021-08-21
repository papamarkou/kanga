# Compute correlation matrix across chains

## Load libraries

library(coda)
library(mcmc)
library(stringr)

## Define function for computing mean correlation matrix across multiple chains

mean_cor <- function(chains) {
  return(Reduce('+', lapply(chains, function(chain) cor(as.matrix(chain))))/length(chains))
}

## Read chains

num_chains <- 4
num_pars <- 3

chains <- vector(mode="list", length=num_chains)
for (i in seq(1, num_chains)) {
  print(paste("Loading chain", str_pad(i, 2, pad='0')))
  chains[[i]] <- mcmc(
    read.table(paste('chain', str_pad(i, 2, pad='0'), '.csv', sep=''), header=FALSE, sep=",")
  )
}

## Compute mean correlation matrix

mean_cor_val <- mean_cor(chains)

print("Mean correlation matrix:")
print(mean_cor_val)

## Compute empirical correlation matrix via crosscorr function of coda, which merges multiple chains into one

crosscorr_val <- crosscorr(mcmc.list(chains))
colnames(crosscorr_val) <- seq(1, num_pars)
rownames(crosscorr_val) <- colnames(crosscorr_val)

print("Correlation matrix across chains provided by coda crosscorr:")
print(crosscorr_val)

## Difference between mean correlation matrix and correlation matrix prrovided by coda crosscorr

cor_val_diff <- mean_cor_val - crosscorr_val

print("Difference between mean correlation matrix and correlation matrix prrovided by coda crosscorr:")
print(cor_val_diff)
