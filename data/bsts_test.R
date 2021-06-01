require(readr)
require(bsts)

df <- read_csv("prInterp.csv")
pr <- ts(df$precipitation, start = c(2013,01,01),
         end = c(2020,12,31), frequency = 365)

plot(pr, main = 'Daily Precipitation of Natuna Islands',
     xlab = 'time', ylab = 'precipitation (mm/day)')

# local level model
ll_ss <- list()
ll_ss <- AddLocalLevel(state.specification = ll_ss,
                       y = pr)
ll_fit <- bsts(pr, state.specification = ll_ss,
               niter = 1e3)


## forecast 30 day ahead
ll_pred <- predict(ll_fit, horizon = 30)

# local linear trend

llt_ss <- list()
llt_ss <- AddLocalLinearTrend(state.specification = llt_ss, 
                              y = pr)
llt_fit <- bsts(pr, state.specification = llt_ss,
                niter = 1e3)

llt_pred <- predict(llt_fit, horizon = 30)

# local linear trend with seasonality
lts_ss <- list()
lts_ss <- AddLocalLinearTrend(lts_ss, y = pr)
lts_ss <- AddSeasonal(lts_ss, pr, nseasons = 365)
lts_fit <- bsts(pr, state.specification = lts_ss,
                niter = 1e3)

plot(lts_fit, 'components',
     xlab='time index',
     ylab='precipitation (mm/day)')

lts_pred <- predict(lts_fit, horizon = 30)
plot(lts_pred, plot.original = 90,
     xlab='time index',
     ylab='precipitation (mm/day)')

CompareBstsModels(lwd = 4, model.list = list(
  level = ll_fit, trend = llt_fit, season = lts_fit),
  colors = c("forestgreen", "firebrick", "blue4"),
  xlab='time index')