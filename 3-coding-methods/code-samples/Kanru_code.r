####housekeeping
rm(list=ls()) #clears RAM

#changes directory to where data is (you need to put in your directory here)
#
setwd('E:/OneDrive - purdue.edu/2022spring/brad') 
#setwd('G:/IN on-farm/IN_On_Farm/Bard/random sample')
library(sp)
library(raster)
library(gstat)
library(rgdal)
####housekeeping


####ABOUT
# this code samples EM data using quantile breaks
# 1. loads data
# 2. removes outliers
# 3. performs nearest neighbor interpolation
# 4. segregates data into quantiles
# 5. randomly samples from each quantile

#user inputs
#Bard_nogreen <- raster("savi_buffer_nogreen.tif")
Bard051322 <- readGDAL("savi051322brad.tif")
spplot(Bard051322)
nsampTotal <- 20 #total number to sample
nclust <- 5 #numbers of quantiles to sample




#optional, trim data above and below quantile limits, here limits are set at 1%
#plots raw histogram with quanile cutoffs in red
z <- Bard051322@data$band1 #z is the variable to be stratified
x <- coordinates(Bard051322)[,1]
y <- coordinates(Bard051322)[,2]

#Remoives Gaps (NAN)
IDX <- !is.na(z)
z <- z[IDX]
y <- y[IDX]
x <- x[IDX]

hist(z)
quant <- quantile(z, c(0.01, 0.99), na.rm = T)
abline(v = quant, col='red') #plots quantiles

#trims data above and below quantile breaks
test <- (z>quant[1])+(z<quant[2])
IDX <- which((test==2))
z <- z[IDX]
y <- y[IDX]
x <- x[IDX]


#clusters data by quantile (number of quantiles = nclust)
#plots stratifid data
ramp <- colorRampPalette(c('green', 'blue',"yellow","pink","orange"))(nclust)
breaks <- quantile(z, seq(0, 1, length=nclust+1))
z.cut <- cut(z, breaks, labels=seq(1, nclust), include.lowest=T)
plot(x, y, pch='.', col=ramp[z.cut], asp=1)


#stratifdied sampling
set.seed(1111)
nstrat <- ceiling(nsampTotal/nclust)
OUT <- NULL
for(i in levels(z.cut)){
  n <- sum(z.cut==i)
  IDX <- sample(1:n, nstrat)
  TEMP <- cbind(as.numeric(i), x[z.cut==i][IDX], y[z.cut==i][IDX])
  OUT <- rbind(OUT, TEMP)
}

points(OUT[,2], OUT[,3], bg=ramp[OUT[,1]], col='white', pch=23, cex=2, lwd=2)

header <- c('strata', 'EAST', 'NORTH')
write(header, 'SamplePts_nearestNeighbor.txt', ncol=3)
write(t(OUT), 'SamplePts_nearestNeighbor.txt', ncol=3, append=T)


OUT