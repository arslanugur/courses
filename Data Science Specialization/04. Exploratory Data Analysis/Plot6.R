##### 0. Libraries #####
library(tidyverse)
library(RColorBrewer)

##### 1. Reading the data #####
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

##### 2. Selecting and arranging data ##### 
# Selecting motor vehicle sources
scc.short <- unique(SCC$Short.Name)
motor <- grep("Motor", scc.short)
motor.codes <- SCC$SCC[motor]

# Subsetting Baltimore data
Bmore <- filter(NEI, fips == "24510")
bmore.motor.df <- subset(Bmore, SCC %in% motor.codes)
bmore.motor.total.pm <- with(bmore.motor.df, tapply(Emissions, year, sum))

# Subsetting LA data
LA <- filter(NEI, fips == "06037")
LA.motor.df <- subset(LA, SCC %in% motor.codes)
LA.motor.total.pm <- with(LA.motor.df, tapply(Emissions, year, sum))

##### 3. Creating plot #####
png("plot6.png")
#Base and Baltimore
plot(unique(Bmore$year), bmore.motor.total.pm, pch=19, col = "darkmagenta", ylim = c(0,20), xaxt = "n", main = expression("PM"[2.5]* " total emissions from motor vehicle sources - Baltimore vs LA"), ylab = "Total emissions (Tons)", xlab = "Year")
lines(unique(Bmore$year), bmore.motor.total.pm, pch=19, col = "darkmagenta", lwd = 2)
text(unique(Bmore$year), bmore.motor.total.pm + 1.2, round(bmore.motor.total.pm, 3), cex = 0.8, col = "darkmagenta")
axis(side = 1, at = unique(Bmore$year), labels = unique(Bmore$year))

# LA
points(unique(LA$year), LA.motor.total.pm, pch = 19, col = "deepskyblue3")
lines(unique(LA$year), LA.motor.total.pm, col = "deepskyblue3", lwd = 2)
text(unique(LA$year), LA.motor.total.pm - 1.2, round(LA.motor.total.pm, 3), cex = 0.8, col = "deepskyblue3") 

#Legend
legend("topleft", legend = c("Baltimore", "Los Angeles"), lty = c(1,1), col = c("darkmagenta", "deepskyblue3"), bty = "n")
dev.off()

