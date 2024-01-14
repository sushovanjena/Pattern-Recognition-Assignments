# Pattern-Recognition-Assignments
Pattern Recognition at IIT Mandi


<h1 style="font-size:24px;">Assignment 1</h1>
There are 3 types of datasets given below. The details of these three datasets are:

a) ​Linearly separable:​These are 2-dimensional artificial data of 2 classes that are linearly
separable. Each class has 1000 data points.

b) ​Non-linearly separable​: These are 2-dimensional artificial data of 2 classes that are
non-linearly separable. Each class has 1000 data points.

c) ​Real-world: ​Real-world data of 3 classes. (Number of data points for class1 = 2388, class2
= 2164 & for class3 = 2291)

Perform
1. Classification using Bayesian classifier (including parameter estimation and decision)
2. Classification (only for the 2 artificial datasets) when you approximate the pdfs via
normalized histograms (considering independence between features - thus, involving 1D
histogram computations for each of the two features)
In both cases, do the following:
For each task, you can divide the data into training and testing parts.
Build the model with the training data and evaluate its performance using the test data.
A typical training testing ratio can be 80% - 20%
Make a confusion matrix to show your results.
For the artificial datasets, also show a 2D scatter plot for the training data and test data with
different colours. Also, points for different classes should also be shown in different colours.

**SOLUTION**

(a)

Boundary Plot of Linearly Separable data using Bayesian Classifier

![Boundary_Plot_LS](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/f6784f39-d1a8-45fb-b513-c6b1d75275aa)

Boundary Plot of Linearly Separable data using Normalised Histograms

![Boundary_Plot_Histogram_LS](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/eb5bcedb-d002-4331-b117-4f25219db548)

(b)

Boundary Plot of Non-Linearly Separable data using Bayesian Classifier
![Boundary_Plot_NLS](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/6d9c5494-d502-483b-99cd-2fc15d2b97e6)

Boundary Plot of Non-Linearly Separable data using Normalised Histograms
![Boundary_Plot_Histogram_NLS](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/b3e02e66-3cd4-4e40-9aec-514408007677)

(c)

Boundary Plot of Real-world data using Bayesian Classifier
![Boundary_Plot_RealData](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/c76c6d1b-2d50-416f-b30f-24d995aa1883)

Boundary Plot of Real-world data using Normalised Histograms
![Boundary_Plot_Histogram_RealData](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/88d95b2a-59be-4651-a22e-f0883c9594be)




<h1 style="font-size:24px;">Assignment 2</h1>
Classification and Segmentation with clustering
You have to perform the given tasks:

a) For the dataset of Assignment 1, perform classification using k-means clustering for the
non-linearly separable case.

b) Perform k-means clustering-based segmentation of the given image.

I) When using only pixel colour values as features

II) When using both pixel colour and location values as features

(In both cases, display the segmentation output as a colour​ ​image, with different colours
assigned pixels belonging to different clusters, and same colours assigned to pixels
belonging to the same cluster)

**SOLUTION**

(a) 
Classification of Non-linearly seprable data with K-Means Clustering

![kmeans_nls](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/c745236e-4d3c-4c69-83f4-735ae511d2c8)

Accuracy of Test-data = 0.935

(b) K-Means Clustering based Segmentation of the given image

Given Image
![Image](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/db439b79-4e56-4204-8791-7da25f9db267)

(I) When using only pixel colour values as features

![k-means_pixel_k=3](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/f46b0813-751a-48fe-9e5a-8f68d5caf73e)
![k-means_pixel_k=10](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/6501f27a-6a19-41d3-b859-00163637c887)
![kmeans_pixel_k=20](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/8a8d163a-4c43-49f1-98ef-28de1c5f0662)


(II) WHen using both Pixel colour and Location as features

![kmeans_pixel loc_k=3](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/918b3119-b7bf-4448-afda-64a9960ca5d6)
![kmeans_pixel loc_k=10](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/de688f88-e688-4004-9cfa-3aa1a48a6668)
![kmeans_pixel loc_k=50](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/b0f74969-0536-402e-af78-1cd3ede5b4fd)


<h1 style="font-size:24px;">Assignment 3</h1>
Build Bayes classifier using GMM for the given data
a) Non-Linearly Separable data of assignment 1
b) Another set of non-seperable data (with 2000 points in each class)

**SOLUTION**

(a) 
GMM CLustering for classification of Non-linearly separable data

![GMM_NLS](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/7b76418b-73d8-46ee-9219-9222b3cb6dd0)

Classification Accuracy = 100.00 %

(b) 
GMM Clustering for classification of Non-Linearly separable data with 2000 points in each class

![GMM_NLS_2000](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/91827da7-9ca5-4a8b-b42c-de6cc318039c)

Classification Accuracy = 100.00 %


<h1 style="font-size:24px;">Assignment 4</h1>
In this assignment, two types of datasets are given:
1. Linearly separable data
2. Non-linearly separable data
For both of the datasets, perform classification using:
1. Perceptron
2. Multi-layer perceptron
3. SVM
You can use inbuilt functions for SVM only. Take the train-test ratio as 70-30. Also find out the
confusion matrix and compare the performance of each classifier.
Also plot the decision boundaries in each case.

**SOLUTION**

(1) Perceptron Decision Boundary

Linearly-Separable Data
![decision_boundry_LS_Perceptron](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/66a4330a-3a51-490b-a156-2763787c172e)

Non-Linearly Separable Data
![decision_boundry_NLS_Perceptron](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/bd4c1223-83e6-469d-affd-ff78a589a1af)

(2) SVM Decision Boundary

Linearly-Separable Data

![decision_boundry_SVM_LS](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/1b410b3e-047e-4c03-911a-b66fa726bec3)

Non-linearly Separable Data

![decision_boundry_SVM_NLS](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/d7f04869-e0ce-4d00-b5b8-bd45eb12724c)

(3) MLP Decision Boundary

Linearly-Separable Data

![decision_boundry_LS_MLP](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/f4a667b8-cfbf-47de-a833-6c63a3f764fa)

Non-Linearly Separable Data

![decision_boundry_NLS_MLP](https://github.com/sushovanjena/Pattern-Recognition-Assignments/assets/68657215/2491df3a-dba2-4f8f-b4bf-99c3e3698b90)


