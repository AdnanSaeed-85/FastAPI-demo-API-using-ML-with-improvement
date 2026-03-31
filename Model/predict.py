import pandas as pd
import pickle

with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

def predict_it(data: dict):
    data = pd.DataFrame([data])
    prediction = model.predict(data)[0]
    return prediction