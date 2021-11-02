##### 0. Libraries #####

library(tidyverse)
library(RColorBrewer)

##### 1. Reading the data #####
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

##### 2. Selecting and arranging data #####
total.pm <- with(NEI, tapply(Emissions, year, sum))

##### 3. Creating plot #####
png("plot1.png")
barplot(total.pm, main = expression("PM"[2.5]* " total emissions - all sources"), ylab = "Total emissions (Tons)", xlab = "Year", col=brewer.pal(4, "Set1"))
dev.off()
