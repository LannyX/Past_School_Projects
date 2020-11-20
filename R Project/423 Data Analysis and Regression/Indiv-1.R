
#BASIC TEST 
GModel1 <- lm (EU_Sales ~ Platform+ Genre+ Critic_Score + Critic_Count+ User_Score + User_Count, data= GameData)
summary(GModel1)
#0.163 

GModel12 <- lm (EU_Sales ~ Platform+ Genre+ Critic_Score + Critic_Count+ User_Score + User_Count + CriticScore_CriticCount +UserScore_UserCount, data= GameData)
summary(GModel12)
#0.1713 with Some Interaction Term


#Get rid of obs that sales=0 NAME = GD 
GD <- subset(GameData, EU_Sales!=0)
#-----USE GD as DATASET BELOW--------
GModel11 <- lm (EU_Sales ~ Platform+ Genre+ Critic_Score + Critic_Count+ User_Score + User_Count, data= GD)
summary(GModel11)
#0.1645

#Log SALES test
GModel13 <- lm (log(EU_Sales) ~ Platform+ Genre+ Critic_Score + Critic_Count+ User_Score + User_Count, data= GD)
summary(GModel13)
#0.3345

#Log SALES No PLATFORM test 
GModel14 <- lm (log(EU_Sales) ~ Critic_Score + Critic_Count+ User_Score + User_Count, data= GD)
summary(GModel14)
#0.2134


GModel15 <- lm (log(EU_Sales) ~ Platform+ Genre+ log(Critic_Score) + Critic_Count+ User_Score + User_Count, data= GD)
summary(GModel15)
#0.3265

#TRY ALL DATA with sales=0 
GModel16 <- lm (log(EU_Sales +1) ~ Platform+ Genre+ Critic_Score + Critic_Count+ User_Score + User_Count, data= GameData)
summary(GModel16)
#0.3146

#-------------------------------
#Combine platforms from same company 
GameData$PlatForm = ifelse(GameData$Platform=="3DS" |GameData$Platform=="DS"|GameData$Platform=="GBA"|GameData$Platform=="Wii"|GameData$Platform=="WillU","Nintendo",
                           ifelse(GameData$Platform=="PS"|GameData$Platform=="PS2"|GameData$Platform=="PS3"|GameData$Platform=="PS4"|GameData$Platform=="PSP"|GameData$Platform=="PSV","Sony",
                                  ifelse(GameData$Platform=="DC","Sega",ifelse(GameData$Platform=="PC","PC","Microsoft"))))
#Refresh GD
GD <- subset(GameData, EU_Sales!=0)

GModel2 <- lm (log(EU_Sales +1) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + User_Count, data= GD)
summary(GModel2)
#0.2986



#TEST different logs Log all first
GModel21 <- lm (log(EU_Sales +1) ~ PlatForm+ Genre+ log(Critic_Score) + log(Critic_Count)+ log(User_Score) + log(User_Count), data= GD)
summary(GModel21)
#R2 0.3337

GModel22 <- lm (log(EU_Sales +1) ~ PlatForm+ Genre+ log(Critic_Score) + Critic_Count+ log(User_Score) + log(User_Count), data= GD)
summary(GModel22)

#R2 0.3349

GModel23 <- lm (log(EU_Sales +1) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count), data= GD)
summary(GModel23)
#R2 0.3379

table(GD$Genre)
#Action    Adventure     Fighting         Misc     Platform       Puzzle       Racing Role-Playing      Shooter   Simulation 
#1507          219          328          329          361           75          542          578          803          275 
#Sports     Strategy 
#792          253 


GDN = subset(GD, Genre != "Puzzle")

#-----USE GDN as DATASET BELOW--------

GModel3 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count), data= GDN)
summary(GModel3)
#0.385
table(GDN$PlatForm)

#Multicollinearity check 1
GDnum = GDN[,-c(1,2,12,13,14,3,5,6,7)]
cor(GDnum)

#Multicollinearity check 2
vif(GModel3)


set.seed(123)
t <- GDN
partition <- sample(2,nrow(t),replace=T,prob=c(0.8,0.2))
train <- t[partition==1,]
test <- t[partition==2,]
GModel4 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count), data= train)
summary(GModel4)
#0.3824
GPrediction <- predict(GModel4,test)
GActual = test$EU_Sales

cor(GPrediction,GActual)
plot(GPrediction,GActual)


#REMOVE OUTLIERS AND BUILD MODEL AGAIN

#outliers regression method
cooksd <- cooks.distance(GModel3)
#Draw cook distance 
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")
#Add cutoff line
abline(h = 5*mean(cooksd, na.rm=T), col="red")
#Add Tags
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>5*mean(cooksd, na.rm=T),names(cooksd),""), col="red") 
# get influential row numbers
influential = c(which(cooksd>(5*mean(cooksd, na.rm=T))))
View(influential)

# influential observations
head(GDN[influential, ]) 

t2= GDN[-influential,]
#--------t2 used as dataset below NO OUTLIERS-----------
set.seed(123)
partition2 <- sample(2,nrow(t2),replace=T,prob=c(0.80,0.20))
train2 <- t2[partition2==1,]
test2 <- t2[partition2==2,]
GModel41 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count), data= train2)
summary(GModel41)
#0.4286

#log test (Verifiy)
GModel42 <- lm (EU_Sales ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count), data= train2)
summary(GModel42)
#0.3076
GModel43 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ log(Critic_Score) + log(Critic_Count)+ log(User_Score) + log(User_Count), data= train2)
summary(GModel43)
#0.4255
GModel44 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ log(Critic_Score) + Critic_Count+ log(User_Score) + log(User_Count), data= train2)
summary(GModel44)
#0.4261
GModel45 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ log(User_Score) + log(User_Count), data= train2)
summary(GModel45)
#0.4275
#Turns out model4.1 has the best R2
#---------MODEL4.1 is the chosen one--------------

GPrediction2 <- predict(GModel41,test2)
GActual2 = test2$EU_Sales

cor(GPrediction2,GActual2)
plot(GPrediction2,GActual2)


#Multicollinearity check 1
GDnum = t2[,-c(1,2,12,13,14,3,5,6,7)]
cor(GDnum)

#Multicollinearity check 2
vif(GModel41)


#stepwise selection 
step <- stepAIC(GModel41,direction = "backward")
step$anova

#stepwise selection Forward
#------------------CANCELED---------------
model_empty = lm(EU_Sales ~ 1, data=t2)
model_full = GModel41
summary(model_empty)
step_fwd <- stepAIC(model_empty,direction = "forward",scope=list(upper=model_full,lower=model_empty))
summary(step_fwd)
#DOESNT REALLY WORK USE BACKWARD 

#FINAL MODEL INFO
step$anova
summary(GModel41)
sm <- summary(GModel41)
View
#MSE 
SSE = sum(sm$residuals^2)
MSE = SSE/5857
RMSE = sqrt(MSE)
RMSE
MSE

#Part 2
#interaction term test
GModel5 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count) + CriticScore_CriticCount + UserScore_UserCount, data= train2)
summary(GModel5)

GModel51 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count) + CriticScore_CriticCount, data= train2)
summary(GModel51)

#second order term test
t2$CriticC_Sq = t2$Critic_Count^2
t2$CriticS_Sq = t2$Critic_Score^2
t2$UserS_Sq = t2$User_Score^2
t2$UserC_Sq = t2$User_Count^2

set.seed(123)
partition3 <- sample(2,nrow(t2),replace=T,prob=c(0.80,0.20))
train3 <- t2[partition3==1,]
test3 <- t2[partition3==2,]

GModel52 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count) + CriticScore_CriticCount 
                + CriticC_Sq + CriticS_Sq + UserS_Sq + UserC_Sq, data= train3)
summary(GModel52)

#KEEP 53 MODEL 

GModel53 <- lm (log(EU_Sales) ~ PlatForm+ Genre+ Critic_Score + Critic_Count+ User_Score + log(User_Count) + CriticScore_CriticCount 
                + UserScore_UserCount + UserS_Sq, data= train3)
summary(GModel53)

#residual analysis
library(car)
durbinWatsonTest(GModel53)

Res<-GModel53$residuals
str(Res)

sum(GModel53$residuals)
hist(GModel53$residuals, breaks = 100)

mean = mean(GModel53$residuals)
sd = sd(GModel53$residuals)
resid_zscore = (GModel53$residuals - mean) / sd

hist (resid_zscore, breaks =100)
plot(GModel53)


plot(train3$Critic_Score , GModel53$residuals, xlab="Critic Score",ylab="Residuals")
plot(train3$Critic_Count , GModel53$residuals, xlab="Critic Count",ylab="Residuals")
plot(train3$User_Score , GModel53$residuals, xlab="User Score",ylab="Residuals")
plot(log(train3$User_Count) , GModel53$residuals, xlab="log(User Count)",ylab="Residuals")


plot(train3$Critic_Score , resid_zscore, xlab="Critic Score",ylab="Residuals zscore")
plot(train3$Critic_Count , resid_zscore, xlab="Critic Count",ylab="Residuals zscore")
plot(train3$User_Score , resid_zscore, xlab="User Score",ylab="Residuals zscore")
plot(log(train3$User_Count) , resid_zscore, xlab="log(User Count)",ylab="Residuals zscore")

#Trans base on residue vs fitted
t2$SalesTrans <- asin(sqrt(log(t2$EU_Sales)))

