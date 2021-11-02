##### 0. Libraries #####
library(tidyverse)
library(RColorBrewer)

##### 1. Reading the data #####
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

##### 2. Selecting and arranging data ##### 
# Selecting coal combustion-related sources
sectors <- unique(SCC$EI.Sector)
coal <- grep("Coal", sectors)
coal.codes <- SCC$SCC[coal]
# Subseting data frame
coal.df <- subset(NEI, SCC %in% coal.codes)
coal.total.pm <- with(coal.df, tapply(Emissions, year, sum))

##### 3. Creating plot #####
png("plot4.png")
barplot(coal.total.pm, main = expression("PM"[2.5]* " total emissions from coal combustion-related sources"), ylab = "Total emissions (Tons)", xlab = "Year", col=brewer.pal(4, "Set1"))
dev.off()

