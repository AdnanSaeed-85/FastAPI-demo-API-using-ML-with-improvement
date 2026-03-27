from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import user_input
from Model.predict import predict_it
from Model.predict import model, MODEL_VERSION
from schema.api_response import Predicted_respo

app = FastAPI()
        
@app.get('/')
def home_endpoint():
    return {'messages': 'Ensurance premium prediction API'}

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'model_version': MODEL_VERSION,
        'model': model is not None,
        'database': 'No Database yet'
    }

@app.post('/predict', response_model=Predicted_respo)
def prediction_endpoint(data: user_input):
    data = {
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
        'bmi':data.bmi,
        'age_group': data.age_group,
        'city_tier': data.city_tier,
        'lifestyle_risk': data.lifestyle_risk,
    }

    try:
        prediction = predict_it(data)
        return JSONResponse(status_code=200, content={"Predicted category": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))