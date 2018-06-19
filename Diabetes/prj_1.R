#########################################################################################
#Name: Pallavi Dwivedi
#Date: October 16,2016
#Project description: Prediction of Diabetes risk based on blood glucose, blood pressure,
#                     skin thickness, insulin, number of pregnancies, Body mass index
#                     and age (Data source: Kaggle)
#########################################################################################

rm(list=ls())
library(caret)
library(randomForest)
library(rpart)
library(dplyr)
library(rattle)
library(pROC)
library(plyr)
library(party)

## Read the dataset
file <- read.csv("diabetes.csv")

file$Outcome <- ifelse(file$Outcome==1,'yes','no')
file$Outcome <- as.factor(file$Outcome)
colnames(file)[3]  <- "BP"     # Blood pressure
colnames(file)[4]  <- "Skin"   # Skin thickness
colnames(file)[7]  <- "DPF"    # Diabetes Pedigree Function
predictors <- names(file)[names(file) != "Outcome"]


#### Gradient boosting ############################################

set.seed(1234)
splitIndex <- createDataPartition(file[,"Outcome"], p = .75, list = FALSE, times = 1)
training <- file[ splitIndex,]
testing  <- file[-splitIndex,]

Control <- trainControl(method='cv', number=3, returnResamp='none', summaryFunction = twoClassSummary,
                           classProbs = TRUE)

Model <- train(training[,predictors], training[,"Outcome"], 
                  method='gbm', 
                  trControl= Control,  
                  metric = "ROC",
                  preProc = c("center", "scale"))
summary(Model)
print(Model)

predictions <- predict(Model, testing[,predictors], type='raw')
head(predictions)

print(postResample(pred=predictions, obs=as.factor(testing[,"Outcome"])))

# probabilites 
library(pROC)
predictions <- predict(Model, testing[,predictors], type='prob')
head(predictions)

## AUC score
auc <- roc(ifelse(testing[,"Outcome"]=="yes",1,0), predictions[[2]])
print(auc$auc)

#### Random forest ################################################################################

model_rf_1 <- train(Outcome ~., data = training, method="rf", trControl = trainControl(method="cv"), number=5)
#predict_rf <- predict(model_rf, testing, type= "class")
predict_rf_1 <- predict(model_rf_1, testing, type= "raw")
#confusionMatrix(predict_rf, testing$classe)
confusionMatrix(predict_rf_1, testing$Outcome)

