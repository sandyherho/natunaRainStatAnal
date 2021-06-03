
# Bayesian structural time-series script

# Sandy H.S. Herho <herho@umd.edu>
# 2021/06/02

library(readr)
library(bsts)

df <- read_csv("../data/avemonth.csv")
pr <- ts(df$precipitation, start = c(2013,01,01),
         end = c(2020,12,01), frequency = 12)

# local level model
ll_ss <- list()
ll_ss <- AddLocalLevel(state.specification = ll_ss,
                       y = pr)
ll_fit <- bsts(pr, state.specification = ll_ss,
               niter = 1e3)


## forecast 30 day ahead
ll_pred <- predict(ll_fit, horizon = 3)

# local linear trend

llt_ss <- list()
llt_ss <- AddLocalLinearTrend(state.specification = llt_ss, 
                              y = pr)
llt_fit <- bsts(pr, state.specification = llt_ss,
                niter = 1e3)

llt_pred <- predict(llt_fit, horizon = 3)

# local linear trend with seasonality
lts_ss <- list()
lts_ss <- AddLocalLinearTrend(lts_ss, y = pr)
lts_ss <- AddSeasonal(lts_ss, pr, nseasons = 12)
lts_fit <- bsts(pr, state.specification = lts_ss,
                niter = 1e3)

lts_pred <- predict(lts_fit, horizon = 12)
plot(lts_pred, plot.original = 90,
     xlab='time index',
     ylab='precipitation (mm/month)')

CompareBstsModels(lwd = 4, model.list = list(
  level = ll_fit, trend = llt_fit, season = lts_fit),
  colors = c("forestgreen", "firebrick", "blue4"),
  xlab='time index')

