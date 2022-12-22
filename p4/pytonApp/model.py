import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

rf = joblib.load("model/rfc_ml_model.m")
df = pd.DataFrame([47,60,1.02,0,0,0,0,0,0,109,25,1.1,141,4.7,15.8,41,8300,5.2])
print(rf.predict(df.T))

