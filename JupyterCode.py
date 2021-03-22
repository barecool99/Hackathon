import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd


#Ciara: dataset with labels, very important for supervisied learning in ML.
# reading the dataset
data=pd.read_csv(r"C:/Users/MR.SAUGAT/Desktop/Hackathon/hackathonDataset.csv", error_bad_lines=False)


#Catherine: removing duplicated, splitting the database, getting rid of outliers or missing data.
#remove duplicates from dataset
data = data.drop_duplicates()


#splitting the database so diaganosis wont show
X = data.iloc[:,2:32].values
Y = data.iloc[:,1].valuesclear


# double check if there is  ay missing or null data points
data.isnull().sum() 
data.isna().sum()


#remove all rows where "None" is the value in any column
data = data.replace(to_replace='None', value=np.nan).dropna()


data.diagnosis.fillna(value=np.nan, inplace=True)


#Amy: Feature Engineering and Visualisation
#turn every catergorical feature data into numerical data 
#our model only processed numbers.
data['concavity_mean'] = pd.to_numeric(data['concavity_mean'])
data['concave points_mean'] = pd.to_numeric(data['concave points_mean'])
data['concavity_se'] = pd.to_numeric(data['concavity_se'])
data['concave points_se'] = pd.to_numeric(data['concave points_se'])
data['concavity_worst'] = pd.to_numeric(data['concavity_worst'])
data['concave points_worst'] = pd.to_numeric(data['concave points_worst'])


data.info()


#print how many benin and maligant cancer cases and the datatype
print("Cancer data set dimensions : {}".format(data.shape))
data.groupby('diagnosis').size()



#Visualising each features from the dataset
#these features are values for each cell nucleus.
data.groupby('diagnosis').hist(figsize=(12, 12))


#Saugat: Implementing the Random Forest classifier as well as Decision Tree Classifier and comparing the results.
#sklearn is sci kit learn library for Machine learning in Python.
from sklearn.model_selection import train_test_split # split dataset into train and testing stage.
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=42)


# we need to hide diagnosis so our ML model can work
X=data.drop('diagnosis', axis=1)
# predict diagnosis
Y=data['diagnosis'] 


from sklearn.model_selection import train_test_split # split dataset into train and testing stage.
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=42)


# we need to hide diagnosis so our ML model can work
X=data.drop('diagnosis', axis=1)
# predict diagnosis
Y=data['diagnosis'] 


#import Decision Tree Classifier and fit your dataset
from sklearn.tree import DecisionTreeClassifier
dtree= DecisionTreeClassifier() # instantiate 
dtree.fit(X_train, Y_train) #fit 
predictions=dtree.predict(X_test)#predict


#classification report and confusion matrix tells you accuracy of your model.
from sklearn.metrics import classification_report, confusion_matrix


#87-90% accuracy which is very good.
print(confusion_matrix(Y_test, predictions))
print(classification_report(Y_test, predictions))


#lets see how the results above compare to random forest classifier
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,Y_train)


rfc_pred=rfc.predict(X_test)


print(confusion_matrix(Y_test, rfc_pred))
print(classification_report(Y_test, rfc_pred))
#94% accuracy wow.