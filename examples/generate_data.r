# Generate data; example taken from documentation of multiESS function of mcmcse package

## Load libraries

library(mAr)

## Set seed and hyper-parameters

# set.seed(100) # Used for generating chains01.csv
# set.seed(200) # Used for generating chains02.csv
# set.seed(300) # Used for generating chains03.csv
# set.seed(400) # Used for generating chains04.csv

p <- 3
n <- 1e3
omega <- 5*diag(1,p)

## Make correlation matrix var(1) model

foo <- matrix(rnorm(p^2), nrow = p)
foo <- foo %*% t(foo)
phi <- foo / (max(eigen(foo)$values) + 1)

## Simulate output

out <- as.matrix(mAr.sim(rep(0,p), phi, omega, N = n))

## Store output

write.table(out, file="chain.csv", sep=",", row.names=FALSE, col.names=FALSE)
