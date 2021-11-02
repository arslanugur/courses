##### 0. Libraries #####
library(tidyverse)
library

##### 1. Reading the data #####
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

##### 2. Selecting and arranging data ##### 
# Selecting motor vehicle sources
scc.short <- unique(SCC$Short.Name)
motor <- grep("Motor", scc.short)
motor.codes <- SCC$SCC[motor]

#Subseting Baltimore data
Bmore <- filter(NEI, fips == "24510")
bmore.motor.df <- subset(Bmore, SCC %in% motor.codes)
bmore.motor.total.pm <- with(bmore.motor.df, tapply(Emissions, year, sum))

##### 3. Creating plot #####
png("plot5.png")
barplot(bmore.motor.total.pm,  main = expression("PM"[2.5]* " total emissions from motor vehicle sources in Baltimore"), ylab = "Total emissions (Tons)", xlab = "Year", col=brewer.pal(4, "Set1"))
dev.off()

