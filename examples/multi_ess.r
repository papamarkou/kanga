# Compute multivariate ESS using multiESS function of mcmcse package

## Load libraries

library(mcmcse)

## Read chains

chains <- read.table(file="chain01.csv", header=FALSE, sep=",")

## Compute multivariate ESS

print(multiESS(chains))

## Compute multivariate ESS from first principles, by replicating the steps of multiESS function of mcmcse package

approx_via_arp <- function(x)
{
  ar.fit <- ar(x, aic=TRUE, method="yule-walker") #, order.max=2)

  gammas <- as.numeric(acf(x, type="covariance", lag.max=ar.fit$order, plot=FALSE)$acf)

  asympt_var <- ar.fit$var.pred/(1-sum(ar.fit$ar))^2

  if(ar.fit$order != 0)
  {
    foo <- 0
    for(i in 1:ar.fit$order)
    {
      for(k in 1:i)
      {
        foo <- foo + ar.fit$ar[i]*k*gammas[abs(k-i)+1]
      }
    }
    Gamma <- 2*(foo + (asympt_var - gammas[1])/2 *sum(1:ar.fit$order * ar.fit$ar)  )/(1-sum(ar.fit$ar))
  } else{
    Gamma <- 0
  }
  
  return(c(Gamma, asympt_var))
  # result <- cbind(Gamma, asympt_var)
  # colnames(result) <- c("Gamma", "asympt_var")
  # return(result)
}

optimal_batch_size <- function(x)
{
  num_iters <- dim(chains)[1]

  ar_fit <- apply(x, 2, approx_via_arp)^2
  coeff <- ( sum(ar_fit[1,])/sum(ar_fit[2,]) )^(1/3)

  b <- floor((num_iters^(1/3))*coeff)
  if(b == 0) b <- 1

  return(b)
}

optimal_batch_size(chains)

# approx_via_arp(chains[, 1])

apply(chains, 2, approx_via_arp)

num_iters <- dim(chains)[1]
num_pars <-  dim(chains)[2]

# cov_mat <- cov(chains)
