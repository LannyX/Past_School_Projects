#Missing Value Analysis

install.packages("Amelia")


library(Amelia)    # Has one "missmap" function for finding missing values
library(ggplot2)
library(GGally)    # For the ggpairs function
library(corrplot)

summary(hd)
missmap(hd,margins = c(15,15))

hdTemp = hd
range(hdTemp$health__homicides_per_100k, na.rm=T)
range(hdTemp$health__pct_excessive_drinking, na.rm=T)
range(hdTemp$health__pop_per_dentist, na.rm=T)
range(hdTemp$health__pct_low_birthweight, na.rm=T)
range(hdTemp$health__pct_adult_smoking, na.rm=T)
range(hdTemp$health__air_pollution_particulate_matter, na.rm=T)
range(hdTemp$health__motor_vehicle_crash_deaths_per_100k, na.rm=T)
range(hdTemp$health__pop_per_primary_care_physician, na.rm=T)

hdTemp$health__homicides_per_100k = replace(hdTemp$health__homicides_per_100k, is.na(hdTemp$health__homicides_per_100k) == T, 200)
hdTemp$health__pct_excessive_drinking = replace(hdTemp$health__pct_excessive_drinking,is.na(hdTemp$health__pct_excessive_drinking)==T,10)
hdTemp$health__pop_per_dentist = replace(hdTemp$health__pop_per_dentist,is.na(hdTemp$health__pop_per_dentist)==T,100000)
hdTemp$health__pct_low_birthweight = replace(hdTemp$health__pct_low_birthweight,is.na(hdTemp$health__pct_low_birthweight)==T,10)
hdTemp$health__pct_adult_smoking = replace(hdTemp$health__pct_adult_smoking,is.na(hdTemp$health__pct_adult_smoking)==T,10)
hdTemp$health__air_pollution_particulate_matter = replace(hdTemp$health__air_pollution_particulate_matter,is.na(hdTemp$health__air_pollution_particulate_matter)==T,100)
hdTemp$health__motor_vehicle_crash_deaths_per_100k = replace(hdTemp$health__motor_vehicle_crash_deaths_per_100k,is.na(hdTemp$health__motor_vehicle_crash_deaths_per_100k)==T,1000)
hdTemp$health__pop_per_primary_care_physician= replace(hdTemp$health__pop_per_primary_care_physician,is.na(hdTemp$health__pop_per_primary_care_physician)==T,100000)
missmap(hdTemp,margins = c(15,15))

plot(health__homicides_per_100k ~.,data= hdTemp)
plot(health__pct_excessive_drinking ~., data= hdTemp)

plot(health__pop_per_dentist ~., data = hdTemp)

plot(health__pct_low_birthweight ~., data = hdTemp)

plot(health__pct_adult_smoking ~., data = hdTemp)

plot(health__air_pollution_particulate_matter ~., data = hdTemp)

plot(health__motor_vehicle_crash_deaths_per_100k ~., data = hdTemp)

plot(health__pop_per_primary_care_physician ~., data = hdTemp)


