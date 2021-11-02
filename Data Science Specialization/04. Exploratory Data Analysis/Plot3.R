library(tidyverse)
library(RColorBrewer)
##### 1. Reading the data #####
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

##### 2. Selecting and arranging data ##### 
Bmore <- filter(NEI, fips == "24510")
Bmore.total.type <- aggregate(Emissions ~ year + type, Bmore, sum)

##### 3. Creating plot #####
png("plot3.png")
ggplot(Bmore.total.type, aes(year, Emissions, color = type)) +
        geom_line() + 
        ggtitle(expression("PM"[2.5]* " total emissions by source type - Baltimore")) +
        xlab("Year") + 
        ylab("Total emissions (Tons)")
dev.off()
