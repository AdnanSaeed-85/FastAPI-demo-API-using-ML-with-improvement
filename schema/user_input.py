from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

class user_input(BaseModel):
    age: Annotated[int, Field(..., description="User's age", ge=1, le=120)]
    weight: Annotated[float, Field(..., description="User's weight in kg", ge=1)]
    height: Annotated[float, Field(..., description="User's height in meters", gt=0)]
    income_lpa: Annotated[float, Field(..., description="User's salary in LPA", ge=1)]
    smoker: Annotated[Literal[True, False], Field(..., description="Whether the user is a smoker")]
    city: Annotated[str, Field(..., description="User's city")]
    occupation: Annotated[
        Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], 
        Field(..., description="Occupation of the user")
    ]

    @field_validator('city')
    @classmethod
    def city_validation(cls, obj: str) -> str:
        city = obj.strip().title()
        return city

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged'
        else:
            return 'senior'
            
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
