##### 0. Libraries #####
library(tidyverse)
library(RColorBrewer)

##### 1. Reading the data #####
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

##### 2. Selecting and arranging data ##### 
Bmore <- filter(NEI, fips == "24510")
Bmore.total.pm <- with(Bmore, tapply(Emissions, year, sum))

##### 3. Creating plot #####
png("plot2.png")
barplot(Bmore.total.pm,  main = expression("PM"[2.5]* " total emissions (all sources) in Baltimore"), ylab = "Total emissions (Tons)", xlab = "Year", col=brewer.pal(4, "Set1"), ylim = c(0, 3500))
dev.off()

