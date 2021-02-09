import pandas as pd 
import numpy as numpy

from sklearn import ensemble
from sklearn import metrics 
from sklearn import model_selection


 if __name__ == "__main__":
    df = pd.read_csv("../data/mobile-price/train.csv")
    #train
    X = df.drop("price_range",axis=1).values
    y = df.price_range.values

    #n_jobs = -1 ->to use all available processing availabel
    classifier = ensemble.RandomForestClassifier(n_jobs=-1)

    param_grid = {
        "n_estimators": [100,200,300,400],
        "max_depth" :[1,3,5,7],
        "criterion" : ["gini","entropy"],
    }