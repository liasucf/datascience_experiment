#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split 
#pour l'entraînement automatique:
from supervised.automl import AutoML

def load_data(PATH):
       data = pd.read_csv( PATH,encoding='latin-1', sep=";")
       data = data.drop(columns=['date_maj','Unnamed: 26', 'hc', 
              'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'hcnox', 'date_maj' ])
       data = data[data['co2'].isna()==False] 
       y = data['co2'].values
       X = data.drop(columns=['co2'])
       X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
       return X_train, X_test, y_train, y_test
       

def load_model(X_train, X_test, y_train, y_test):

       automl = AutoML(total_time_limit=5*60,mode='Explain',random_state=42,ml_task='regression', algorithms=["Decision Tree"])
       #fit models
       automl.fit(X_train,y_train)
       #predictions
       predictions = automl.predict(X_test)
       #generate html report
       return automl

 