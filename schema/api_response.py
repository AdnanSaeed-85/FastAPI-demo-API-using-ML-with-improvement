from typing import Dict, Annotated
from pydantic import BaseModel, Field

class Predicted_respo(BaseModel):
    prediction_class: str = Field(..., description='The predicted insurance premium category', examples=['High'])