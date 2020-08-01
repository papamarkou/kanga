# Compute multivariate ESS using multiESS function of mcmcse package

## Load libraries

library(mcmcse)

## Read chains

chains <- read.table(file="chain01.csv", header=FALSE, sep=",")

## Compute multivariate ESS

print(multiESS(chains))

## Compute multivariate ESS from first principles, by replicating the steps of multiESS function of mcmcse package

num_iters <- dim(chains)[1]
num_pars <-  dim(chains)[2]

# cov_mat <- cov(chains)

chain = chains[, 1]

ar.fit <- ar(chain, aic=TRUE)

gammas <- as.numeric(acf(chain, type="covariance", lag.max=ar.fit$order, plot=FALSE)$acf)

asympt_var <- ar.fit$var.pred/(1-sum(ar.fit$ar))^2

if(ar.fit$order != 0)
{
  foo <- 0
  for(i in 1:ar.fit$order)
  {
    for(k in 1:i)
    {
      foo <- foo + ar.fit$ar[i]*k*gammas[abs(k-i)+1]
      print(foo)
    }
  }
  Gamma <- 2*(foo + (asympt_var - gammas[1])/2 *sum(1:ar.fit$order * ar.fit$ar)  )/(1-sum(ar.fit$ar))
} else{
  Gamma <- 0
}
