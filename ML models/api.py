import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import json
import pickle

from fastapi.templating import Jinja2Templates
from keras.preprocessing import sequence
import keras
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class churn_model(BaseModel):
    CreditScore: int()
    Age: int()
    Tenure :int()
    Balance: int()
    NumOfProducts : int()
    HasCrCard: bool()
    IsActivaMembar: bool()
    EstimatedSalary: int()
    Geography_Germarny : int()
    Gegraphy_Spain: int()
    Gender_Male: bool()

class credit_model(BaseModel):

    gender: str()
    car: str()
    property:str()
    children:int()
    annual_income: float()
    income_type: str()
    family_status: str()
    housing_type: str()
    work_phone : int()
    phone:int()
    email:int()
    occupation_type : str()
    fam_members:float()
    age: float()
    year_of_employment: float()
    target: int()


templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="./static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

credit_load_model= pickle.load(open('./Final_Sentiment_Tokenizer.pickle', 'rb'))

churn_load_model=keras.models.load_model("./Final_Sentiment_Analysis.h5")
with open('./Final_Sentiment_Tokenizer.pickle', 'rb') as handle:
   churn_model_load = pickle.load(handle)

# ------------------credit score------------------------
@app.post('/credit_score')
async def predict(input_parameters: credit_model): 
    print(input_parameters)
    input_data = await input_parameters.json()
    input_dictionary = json.loads(input_data)

    CreditScore = input_dictionary['CreditScore']
    Age = input_dictionary['Age']
    Tenure = input_dictionary['Tenure']
    Balance = input_dictionary['Balance']
    NumOfProducts  = input_dictionary['NumOfProducts']
    HasCrCard = input_dictionary['HasCrCard']
    IsActivaMembar = input_dictionary['IsActivaMembar']
    EstimatedSalary= input_dictionary['EstimatedSalary']
    Geography_Germarny = input_dictionary['Geography_Germarny']
    Gegraphy_Spain= input_dictionary['Gegraphy_Spain']
    Gender_Male = input_dictionary['Gender_Male']

    input_list = [CreditScore,Age, Tenure, Balance, NumOfProducts,HasCrCard , IsActivaMembar,EstimatedSalary, Geography_Germarny, Gegraphy_Spain, Gender_Male]
    
    prediction = credit_model_load.predict([input_list])

    return prediction

# -------------------------Churn Model-------------------------------
@app.post('/churn_score')
async def predict(input_parameters: churn_model): 
    print(input_parameters)
    input_data_churn = await input_parameters.json()
    input_dictionary_churn = json.loads(input_data_churn)

    gender = input_dictionary_churn['gender']
    car = input_dictionary_churn['car']
    property = input_dictionary_churn['property']
    children = input_dictionary_churn['children']
    annual_income = input_dictionary_churn['annual_income']
    income_type = input_dictionary_churn['income_type']
    family_status = input_dictionary_churn['family_status']
    housing_type= input_dictionary_churn['housing_type']
    work_phone = input_dictionary_churn['work_phone']
    phone = input_dictionary_churn['phone']
    email = input_dictionary_churn['email']
    occupation_type = input_dictionary_churn['occupation_type']
    fam_members = input_dictionary_churn['fam_members']
    age = input_dictionary_churn['age']
    year_of_employment= input_dictionary_churn['year_of_employment']
    target = input_dictionary_churn['target']

    input_list_churn = [gender,car,property,children,annual_income,income_type,family_status,housing_type,work_phone,phone,email ,
                  occupation_type,fam_members, age ,year_of_employment,target]
    
    prediction = credit_model_load.predict([input_list_churn])

    if prediction[0]==0:
        return 'true'
    else: 
        return 'false'


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)