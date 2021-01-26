import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np


@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict_diabetes(request):
    try:
        Pregnancies = request.data.get('Pregnancies',None)
        Glucose = request.data.get('Glucose',None)
        BloodPressure = request.data.get('BloodPressure',None)
        SkinThickness = request.data.get('SkinThickness',None)
        Insulin = request.data.get('Insulin',None)
        BMI = request.data.get('BMI',None)
        DiabetesPedigreeFunction = request.data.get('DiabetesPedigreeFunction',None)
        Age = request.data.get('Age',None)
        fields = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        if not None in fields:
            Pregnancies = float(Pregnancies)
            Glucose = float(Glucose)
            BloodPressure = float(BloodPressure)
            SkinThickness = float(SkinThickness)
            Insulin = float(Insulin)
            BMI = float(BMI)
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
            Age = float(Age)
            result = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            model_name = 'ml_model/model_diabetes.pkl'
            input_data = pickle.load(open(model_name, 'rb'))
            prediction = input_data.predict([result])[0]
            conf_score =  np.max(input_data.predict_proba([result]))*100
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : prediction,
                'confidence_score' : conf_score
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }
    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)