from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated

# pydantic model to validate incoming data
class UserInput(BaseModel):
    Age: Annotated[int, Field(..., ge=0, le=120 , description="Age of the patient")]
    Diabetes: Annotated[Literal[0, 1], Field(..., description="Whether the patient has diabetes")]
    BloodPressureProblems:Annotated[Literal[0, 1], Field(..., description="Whether the patient has blood pressure problems")]
    AnyTransplants: Annotated[Literal[0, 1], Field(..., description="Whether the patient has any transplants")]
    AnyChronicDiseases: Annotated[Literal[0, 1], Field(..., description="Whether the patient has any chronic diseases")]
    Height: Annotated[float, Field(..., ge=0, description="Height of the patient in cm")]
    Weight: Annotated[float, Field(..., ge=0, description="Weight of the patient in kg")]
    KnownAllergies: Annotated[Literal[0, 1], Field(..., description="Whether the patient has known allergies")]
    HistoryOfCancerInFamily: Annotated[Literal[0, 1], Field(..., description="Whether there is a history of cancer in the family")]
    NumberOfMajorSurgeries: Annotated[int, Field(..., ge=0, description="Number of major surgeries the patient has had")]

    @computed_field
    @property
    def BMI(self) -> float:
        return round(self.Weight / ((self.Height / 100) ** 2), 2)
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.Age < 30:
            return "Young"
        elif self.Age < 45:
            return "Adult"
        elif self.Age < 60:
            return "Middle_Age"
        return "Senior"