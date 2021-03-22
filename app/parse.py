import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

#import Decision Tree Classifier and fit your dataset
from sklearn.model_selection import train_test_split # split dataset into train and testing stage.
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#classification report and confusion matrix tells you accuracy of your model.
from sklearn.metrics import classification_report, confusion_matrix

from app import app


#Ciara: dataset with labels, very important for supervisied learning in ML.
class ParseDataset:
    # Could create another function to read the dataset from the DB and use that instead of/as well as .csv dataset?
    def read_dataset():
        # reading the dataset
        dataset_path = app.config['DATA_SET']

        data = pd.read_csv(dataset_path, error_bad_lines=False)

        return data


#Catherine: removing duplicated, splitting the database, getting rid of outliers or missing data.
class CleanDataset:
    def clean_dataset():
        data = ParseDataset.read_dataset()


        #remove duplicates from dataset
        data = data.drop_duplicates()


        # #splitting the database so diaganosis wont show
        # X = data.iloc[:,2:32].values
        # Y = data.iloc[:,1].values


        # double check if there is  ay missing or null data points
        data.isnull().sum() 
        data.isna().sum()


        #remove all rows where "None" is the value in any column
        data = data.replace(to_replace='None', value=np.nan).dropna()


        data.diagnosis.fillna(value=np.nan, inplace=True)

        return data


#Amy: Feature Engineering and Visualisation
class GenerateGraphs():
    def graphs():
        data = CleanDataset.clean_dataset()

        #turn every catergorical feature data into numerical data 
        #our model only processed numbers.
        data['concavity_mean'] = pd.to_numeric(data['concavity_mean'])
        data['concave points_mean'] = pd.to_numeric(data['concave points_mean'])
        data['concavity_se'] = pd.to_numeric(data['concavity_se'])
        data['concave points_se'] = pd.to_numeric(data['concave points_se'])
        data['concavity_worst'] = pd.to_numeric(data['concavity_worst'])
        data['concave points_worst'] = pd.to_numeric(data['concave points_worst'])


        # data.info()


        #print how many benin and maligant cancer cases and the datatype
        print("Cancer data set dimensions (Rows, Columns) : {}".format(data.shape))
        data.groupby('diagnosis').size()


        # #Visualising each features from the dataset
        # #these features are values for each cell nucleus.
        # graph = data.groupby('diagnosis').hist(figsize=(12, 12)) 
        # Moved to for loop - tried making into var but didn't work :|

        x = 0
        for graphs in data.groupby('diagnosis').hist(figsize=(12, 12)):
            x += 1

            # Saves the graphs as a PNG so that it can be displayed on webpage
            plt.savefig('app/static/images/graph' + str(x) + '.png') # Would be nice if we could concatenate the graph type (mal/ben) rather than graph1.  
            plt.close()                                              # was unsure how to extract the diagnosis detail to do that though :|

        # return graph


class MachineLearning():
    def getMLAccuracy():
            data = CleanDataset.clean_dataset()

            X = data.iloc[:,2:32].values
            Y = data.iloc[:,1].values

            X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=42)

            # we need to hide diagnosis so our ML model can work
            X=data.drop('diagnosis', axis=1)
            # predict diagnosis
            Y=data['diagnosis'] 


            dtree= DecisionTreeClassifier() # instantiate 
            dtree.fit(X_train, Y_train) #fit 
            predictions=dtree.predict(X_test)#predict


            #87-90% accuracy which is very good.
            # print(confusion_matrix(Y_test, predictions))
            # print(classification_report(Y_test, predictions))


            #lets see how the results above compare to random forest classifier
            rfc=RandomForestClassifier(n_estimators=200)
            rfc.fit(X_train,Y_train)


            rfc_pred=rfc.predict(X_test)

            # print(confusion_matrix(Y_test, rfc_pred))
            # print(classification_report(Y_test, rfc_pred))

            # 94% accuracy wow
            report = classification_report(Y_test, rfc_pred, output_dict = True)
            dataFrame = pd.DataFrame(report).transpose()


            return dataFrame