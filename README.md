# Medical_insurance_premium_api

A Machine Learning–powered FastAPI application that predicts health insurance premium prices based on user health and medical history.

This project demonstrates end-to-end ML deployment — from model training to serving predictions through a REST API.

 Features

✅ Predicts insurance premium using ML
✅ FastAPI backend for high performance
✅ Input validation using Pydantic
✅ Automatic BMI calculation
✅ Age grouped into risk categories
✅ Clean and production-ready API design

 Dataset

The model was trained on a dataset containing:

Age Group (Young, Adult, Middle_Age, Senior)

BMI

Diabetes status

Blood pressure problems

Transplant history

Allergies

Cancer history in family

Number of major surgeries

Premium Price (Target)

 Machine Learning

Algorithm: RandomForestRegressor

Encoding: OneHotEncoder for categorical features

Model persistence: Pickle / Joblib

Library: Scikit-learn

🛠️ Tech Stack

Python

FastAPI

Scikit-learn

Pandas

Uvicorn

Pydantic

▶️ Run Locally (Without Docker)
1️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

4️⃣ Open in browser
http://localhost:8000/docs

🐳 Run Using Docker
1️⃣ Build Docker image
docker build -t medical-insurance-premium-api .

2️⃣ Run Docker container
docker run -p 8000:8000 medical-insurance-premium-api

3️⃣ Access API

Swagger UI:

http://localhost:8000/docs


Health check:

http://localhost:8000/health

📦 Docker Image (Docker Hub)
docker pull sunaina14/medical-insurance-premium-api:latest


Run:

docker run -p 8000:8000 sunaina14/medical-insurance-premium-api:latest 

Future Improvements

Add input validation & error handling

Add logging

Deploy on AWS EC2 / ECS

CI/CD using GitHub Actions

Add model versioning

Add monitoring

👩‍💻 Author

*Note this is only for educational purpose 
Sunaina Khan
📌 Learning ML Deployment | FastAPI | Docker | AWS
