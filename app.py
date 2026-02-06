from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output , MODEL_VERSION, model
from schema.user_input import UserInput


    
app = FastAPI()

    
# human readable endpoints
@app.get("/")
def home():
    return {"message": "Welcome to the Health Insurance Premium Prediction API!"}

#machine readable endpoint
@app.get("/health")
def health_check():
    return {"status": "API is running smoothly.",
            "version": MODEL_VERSION,
            "model_loaded": model is not None
            } 
        

@app.post("/predict")
def predict_premium(input_data: UserInput):
    try:
        # Create a dictionary with EVERY possible column name
        user_input = {
            "Age": input_data.Age,
            "Diabetes": input_data.Diabetes,
            "BloodPressureProblems": input_data.BloodPressureProblems,
            "AnyTransplants": input_data.AnyTransplants,
            "AnyChronicDiseases": input_data.AnyChronicDiseases,
            "KnownAllergies": input_data.KnownAllergies,
            "HistoryOfCancerInFamily": input_data.HistoryOfCancerInFamily,
            "NumberOfMajorSurgeries": input_data.NumberOfMajorSurgeries,
            "BMI": input_data.BMI,
            "Age_group": input_data.age_group
        }
        
    
        # Make prediction
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content=prediction)
    
    except Exception as e:
        # This part is key: It prints the real error to your terminal
        print("\n" + "="*50)
        print(f"MODEL ERROR: {e}")
        print("="*50 + "\n")
        
        return JSONResponse(status_code=500,content={"error": str(e)})