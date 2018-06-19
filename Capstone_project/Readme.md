# MLND Capstone Project

##Project Overview
The Amazon basin contains the world’s largest rainforest, which is home to the most diverse and numerous arrays of plant and animal species in the world. The continued deforestation of the Amazon forest contributes towards reduction in biodiversity, habitat loss, climate change and other devastating effects (Kaggle). The several causes of deforestation in the Amazon basin include human causes such as farming, housing, mall-scale 
subsistence agriculture, and serving as a resource for cattle pasture, valuable hardwoods as well as natural causes. The data regarding the location of deforestation of the Amazon forest can help governments and local stakeholders respond more quickly and effectively to prevent deforestation.

The Earth-imaging satellites such as Landsat and MODIS have been collecting coarse-resolution image data (30 meter pixels and 250 meter pixels respectively) to track changes in forest for past several years. The current project was based on the image data collected by Earth-imaging 
satellite, built by Planet and its Brazilian partner SCCON, at 3-5 meter resolution to label satellite image chips with atmospheric conditions and various classes of land cover or land use (Kaggle).

##Problem Statement
The goal of the project was to track changes in the Amazon rainforest due to deforestation using the satellite image data collected by Planet and its Brazilian partner SCCON. The satellite data was used to classify the Amazon rainforest land surface into the following categories or classes (Planet labs):
1. Primary (primary rainforest): Area in the forest that exhibits dense 
tree cover.
2. Artisinal mining: Small scale mining operations, often illegal, for 
extraction of gold, which results in deforestation and deep pits near 
rivers.
3. Bare ground: Naturally occurring tree free areas that are not the 
result of human activity.
4. Slash burn: Cutting and burning of plants in the forest to create a 
field for farming.
5. Conventional mining: Large-scale legal mining operations in the 
forest.
6. Blow down: Uprooting of trees by due to storm or high-speed winds.
7. Selective logging: Selectively cutting down one or two species of 
trees while leaving the rest intact.
8. Blooming: Natural phenomenon where particular species of tees 
bloom, flower and fruit at the same time.
9. Habitation: Homes or buildings.
10. Road
11. Water

The natural causes of deforestation include blow down and bare ground 
and the human causes of deforestation include artisinal mining, conventional mining, slash burn, selective logging and habitation. The satellite image labels were combination of weather labels ('clear', 'partly cloudy', 'haze', 'cloudy') and the above categories.

##Outline of tasks. 
The satellite image data, used for this project, was obtained from Kaggle website (Kaggle-data). A sample of 300 images was drawn from the training data set (train-tif-v2.tar.7z). The satellite image data was pre-processed using Principal Component Analysis. The preprocessed data was then split into training (285 images) and test (15 images) datasets. The training data set was used for training the Support Vector Machine classification model in order to classify the land cover. The target variable (labels), which was used the classification of the training data, can be found in the ‘train.csv’ dataset on the Kaggle website (Kaggledata).

##Metrics

To evaluate the performance of the SVM classifier, overall accuracy score was estimated using a ten-fold cross-validation. Overall accuracy is defined as the total number of correctly classified images divided by the total number of images. The classification accuracy score has been used as the measure for evaluation of performance of SVM classifier on the satellite image data by several previous studies (Elmannai et al., 2013; He at al.,2017; Wieland et al., 2014).


##The project required the following libraries:
• opencv-python
• libgtk2.0-dev (required for installation of opencv-python)
• os
• glob
• sklearn
• numpy
• pandas
• seaborn
• matplotlib
• mlxtend

Kaggle: https://www.kaggle.com/c/planet-understanding-the-amazonfrom-space
Kaggle-data:https://www.kaggle.com/c/planet-understanding-the-amazonfrom-space/data
Wikipedia: https://en.wikipedia.org/wiki/Multispectral_image
Planet labs : https://github.com/planetlabs/planet-amazon-deforestation
