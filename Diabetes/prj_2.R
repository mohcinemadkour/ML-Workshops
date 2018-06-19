rm(list=ls())
library(BAS)
library(caret)
library(ROCR)

file <- read.csv("diabetes.csv")
colnames(file)[3]  <- "BP"     # Blood pressure
colnames(file)[4]  <- "Skin_Th"   # Skin thickness
colnames(file)[7]  <- "DPF"    # Diabetes Pedigree Function

set.seed(1234)
splitIndex <- createDataPartition(file[,"Outcome"], p = .75, list = FALSE, times = 1)
training <- file[ splitIndex,]
testing  <- file[-splitIndex,]

##### Bayesian adaptive sampling for variable selection and model averaging ###################################################

mod_1 = bas.glm(Outcome~ ., data=training, method="BAS", family=binomial(),
                 betaprior=hyper.g.n(), modelprior=uniform())

# mod_1 = bas.glm(Outcome~ ., data=training, n.models= 2^7, method="BAS",
#                 betaprior=CCH(a=1, b=nrow(training)/2, s=0), family=binomial(),
#                 modelprior=uniform())

pred_1 = predict(mod_1, newdata= testing, top=1)  # Highest Probability model

# pred_1 = predict(mod_1, newdata= testing, se.fit=FALSE, 
#                  type=c("response", "link"), top=NULL,
#                  estimator="BMA", prediction=FALSE)
# 
cv.summary.bas(pred_1$fit, testing$Outcome,score="miss-class")
## missclass error = 0.208333

plot(mod_1,ask=F, which=4, caption="", sub.caption="")

mod_1
summary(mod_1)
image(mod_1, rotate=F)

############ variable selection using stepwise regression #######################################

mod_2 = glm(Outcome~ ., data=training, family='binomial')
reg = step(mod_2, direction="both")
## Best model: AIC=568.15
## Outcome ~ Pregnancies + Glucose + BMI + DPF
anova(mod_2, test="Chisq")
fitted.results <- predict(mod_2,newdata= testing,type='response')
fitted.results <- ifelse(fitted.results > 0.5,1,0)

misClasificError <- mean(fitted.results != testing$Outcome)
print(paste('Accuracy',1-misClasificError))
## "Accuracy= 0.791666666666667"

pred_2 <- predict(mod_2, newdata=testing, type="response")
pr <- prediction(pred_2, testing$Outcome)
perf <- performance(pr, measure = "tpr", x.measure = "fpr")

auc <- performance(pr, measure = "auc")
auc <- auc@y.values[[1]]
auc

plot(perf)
## ROC curve (Area under the curve = 0.852)
