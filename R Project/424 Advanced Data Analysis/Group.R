# data cleaning 
hd = heart_disease
dt = na.omit(hd)
dt = dt[,-1]
# rename column names
cnames=paste("v",1:22,sep="")
cnames=c('mort',cnames)
cnames
colnames(dt)=cnames
colnames(hd)
# data transfromation 
dt$v2 = log(dt$v2+1)
dt$v4 = log(dt$v4+1)
dt$v7 = log(dt$v7+1)
dt$v12= log(dt$v12+1)
dt$v16= log(dt$v16+1)
dt$v17= log(dt$v17+1)
dt$v18= log(dt$v18+1)
dt$v19= log(dt$v19+1)
dt$v8 = sqrt(dt$v8)
dt$v11 = sqrt(dt$v11)
hist(dt$v16)

# save the dataset
write.csv(dt,"D:\\clean_hd.csv",row.names = FALSE)


library(psych)
dt_noncate=dt[,-c(21:23)]
bartlett.test(dt_noncate)
KMO(dt_noncate)

# LASSO
# split the dataset to training and testing sets 
set.seed(168)
partition = sample(2,nrow(dt),replace=T,prob=c(0.80,0.20))
train = dt[partition==1,]
test = dt[partition==2,]

# Separate the X's and Y's as matrices
xTrain = as.matrix(train[, -c(1,21:23)])   # Take out column 1 and cate col 21:23
yTrain = as.matrix(train[, 1])    # Take only column 1

xTest = as.matrix(test[, -c(1,21:23)])   # Take out column 1
yTest = as.matrix(test[, 1])    # Take only column 1

#OLS
OLS = lm (mort ~ ., data = train)
summary(OLS)
#find RMSE
rmseTrain = sqrt(mean(OLS$residuals^2))
rmseTrain
#predict on the test set and RMSE of test set
olsPredict = predict(OLS, test)
rmseTest = sqrt(mean((olsPredict - test$mort)^2))
rmseTest
library(car)

#LASSO
library(glmnet)
fitLasso = cv.glmnet(xTrain, yTrain, alpha=1)
fitLasso
plot(fitLasso)
summary(fitLasso)
fitLasso$lambda.1se
fitLasso$lambda.min
# 
plot(fitLasso,xvar="lambda",lable=TRUE)
# select 
lassoPred = predict(fitLasso, xTest, s="lambda.min")
rmseLasso = sqrt(mean((lassoPred - yTest)^2))
rmseLasso
lassoPred_p = predict(fitLasso, xTrain, s="lambda.min")
rmseLasso_p = sqrt(mean((lassoPred_p - yTrain)^2))
rmseLasso_p
# 
coef(fitLasso, s=fitLasso$lambda.min)
fit = glmnet(xTrain, yTrain, alpha=1, nlambda = 20)
print(fit)



dt = clean_hd

# PCA 
summary(dt)
pca = prcomp(dt[,1:20],scale. = T)
summary(pca)
#print(pca)
plot(pca)

abline(h=1,lwd=1,col="blue")
# principal factor
library(corrplot)
cor = cor(dt[,-c(1,21:23)])
corrplot(cor, order="AOE",method="ellipse")
corrplot(cor,method = "ellipse",tl.pos = NULL, tl.cex = 0.65,order="AOE") 
corrplot(cor,type="upper",order="AOE",method = "ellipse")
corrplot(cor,add=TRUE, type="lower", method="number",diag=FALSE, cl.pos="n",order="AOE")
library(psych)
p2 = principal(dt[,2:20],nfactor =4, rotate="varimax")
print(p2$loadings,cutoff=.4)

# f
round(cor_em,2)
corTest = corr.test(dt[,2:20],adjust="none")
round(corTest$p,2)
MTest=ifelse(corTest$p<0.05, T, F)
MTest
colSums(MTest)-1
# delete over correlated v13 v18
fa = dt[,-c(14,19,21:23)]
faA = principal(fa,nfactor =4, rotate="varimax")
print(faA$loadings,cutoff=.4)


#
faA = principal(fa,nfactor = 4, rotate="varimax", n.obs= 1069)
summary(faA)
#print(faA)

pchisq(2065.19, df = 48, lower.tail = FALSE)
cfa = factanal(fa,4)
print(cfa$loadings,cutoff = 0.4)



# LDA
source("Confusion.R")
v20= train[,-c(22:23)]
lda_v20 = lda(v20 ~ ., data = v20)
v20.values = predict(lda_v20)
table(v20$v20,v20.values$class)
confusion(v20.values$class,v20$v20)
v20_test = test [,-c(22:23)]
v20_test.values = predict (lda_v20,v20_test)
confusion(v20_test.values$class,v20_test$v20)

v21= train[,-c(21,23)]
lda_v21 = lda(v21 ~ ., data = v21)
v21.values = predict(lda_v21)
table(v21$v21,v21.values$class)
confusion(v21.values$class,v21$v21)

# rename the V20
dt$v20 = ifelse(dt$v20 == "A1","Metro_1",
                ifelse(dt$v20== "A2","Metro_2",
                       ifelse(dt$v20== "A3","Metro_3",
                              ifelse(dt$v20== "B1","Rural_A",
                                     ifelse(dt$v20== "B2","Rural_N",
                                            ifelse(dt$v20== "C1","City_A",
                                                   ifelse(dt$v20== "D1","City_N",
                                                          ifelse(dt$v20== "C2","SmallCity_A","SmallCity_N"))))))))
dt$v23 = ifelse(dt$v20 == "Metro_1" |dt$v20 == "Metro_2"|dt$v20 == "Metro_3" ,"Metro" ,
                ifelse(dt$v20== "Rural_A"|dt$v20== "Rural_N" ,"Rural",
                       ifelse(dt$v20== "City_A"|dt$v20== "City_N","City","SmallCity")))
set.seed(166)
partition = sample(2,nrow(dt),replace=T,prob=c(0.80,0.20))
train = dt[partition==1,]
test = dt[partition==2,]

#LDA NEW
v20= train[,-c(22:24)]
lda_v20 = lda(v20 ~ ., data = v20)
v20.values = predict(lda_v20)
table(v20$v20,v20.values$class)
confusion(v20.values$class,v20$v20)
v20_test = test [,-c(22:24)]
v20_test.values = predict (lda_v20,v20_test)
confusion(v20_test.values$class,v20_test$v20)

v23= train[,-c(21:23)]
lda_v23 = lda(v23 ~ ., data = v23)
v23.values = predict(lda_v23)
confusion(v23.values$class,v23$v23)


