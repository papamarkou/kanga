# Compute R potential scale reduction factor across chains using Rhat function of rstan package

## Load libraries

library(rstan)
library(stringr)

## Read chains

num_iters <- 1000
num_chains <- 4
num_pars <- 3

chains <- array(data=NA, dim=c(num_iters, num_chains, num_pars))
for (i in seq(1, num_chains)) {
  print(paste("Loading chain", str_pad(i, 2, pad='0')))
  chains[, i, ] <- as.matrix(read.table(paste('chain', str_pad(i, 2, pad='0'), '.csv', sep=''), header=FALSE, sep=","))
}

## Compute rhat

rhat_vals <- vector(mode="numeric", length=num_pars)
for (i in seq(1, num_pars)) {
  rhat_vals[i] <- Rhat(chains[, , i])
}

print(rhat_vals)
