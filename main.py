# Import Section
import time # Potential usage, tbd
import requests # Also potential, assuming we have to query PharmGKB


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.input import SimpleImputer
from sklearn.decomposition import TruncatedSVD
from sklearn.svm import SVC
from sklearn.metric import (
        accuracy_score,
        precision_score,
        recall_score,
        classification_report,
        confusion_matrix,
    )


# Data Input / Loading / Cleaning
file path = "" # Change based on own file path (copy + paste)
df = pd.read_csv(file_path)

print(f"Loaded dataset: {df.shape[0]} compunds, {df.shape[1]} columns.")
print(f"Class distribution: \n{df['Class'].value_counts()}\n")

#Seperate target labels, identifiers & descriptors
compoundID = df["CID"]
y = df["Class"]


#Drop
colsToDrop = ["CID", "Class"]
if "PUBCHEM_COORDINATE_TYPE" in df.columns:
    cols_to_drop.append("PUBCHEM_COORDINATE_TYPE")

x = df.drop(columns=colsToDrop)

x = x.apply(pd.to_numeric, errors="coerce") #turn text-formatted nums into math-ready nums and anything else NaN


# Data Processing


# Model Training

# Model Eval.


# Screening
