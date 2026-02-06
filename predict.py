
import pandas as pd
import joblib  


# Constants
# ==========================
MODEL_PATH = "model/model.pkl"  
MODEL_VERSION = "1.0.0"  


# Load Model
# ==========================
try:
    model = joblib.load("model/model.pkl")
except Exception as e:
    raise RuntimeError(f"Failed to load model from {MODEL_PATH}: {e}")


# Categorization Function
# ==========================
def categorize_premium(premium: float) -> str:
    """
    Categorize premium into Low, Medium, High.
    Adjust thresholds based on your dataset.
    """
    if premium < 20000:
        return "Low"
    elif premium < 35000:
        return "Medium"
    else:
        return "High"

# Prediction Function
# ==========================
def predict_output(user_input: dict) -> dict:
    """
    Predict health insurance premium and category.

    Args:
        user_input (dict): A dictionary of input features for the model.

    Returns:
        dict: Predicted premium, category, and model version.
    """
    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])

    # Get model prediction
    prediction = model.predict(input_df)

    # Always take first element
    prediction = prediction[0]

    #  SAFELY extract premium
    if isinstance(prediction, dict):
        premium = prediction.get("Predicted_Health_Insurance_Premium")
    else:
        premium = prediction

    #  Validate premium
    if not isinstance(premium, (int, float)):
        raise ValueError("Model returned invalid premium value")

    premium = float(premium)

    # Categorize
    category = categorize_premium(premium)

    return {
        "Predicted_Health_Insurance_Premium": round(premium, 2),
        "Predicted_Category": category,
        "Model_Version": MODEL_VERSION
    }



