# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:11:14 2020

@author: Asus
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import QDate, Qt, QDateTime
import sys
import pandas as pd
import pickle
import datetime


class DiabetesApp(QMainWindow):
    def __init__(self):
        super(DiabetesApp, self).__init__()
        uic.loadUi("diabetescheck.ui", self)
        self.submit.clicked.connect(self.form)
        self.clear.clicked.connect(self.clear_data)
        self.show()
        
    def form(self):
        #now = QDate.currentDate()
        now = QDateTime.currentDateTime()
        model_name = 'model_diabetes.pkl'
        #self.model = pd.read_pickle(model_name)
        self.model = pickle.load(open(model_name, 'rb'))
        Name = self.name.text()
        Pregnancies = int(self.pregnancies.text())
        Glucose = int(self.glucose.text())
        BloodPressure = int(self.bloodpressure.text())
        SkinThickness = int(self.skinthickness.text())
        Insulin = int(self.insulin.text())
        BMI = float(self.bmi.text())
        DiabetesPedigreeFunction = float(self.dpf.text())
        Age = int(self.age.text())        
        self.result = self.model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                 BMI, DiabetesPedigreeFunction, Age]])
        if self.result == ["Normal"]:
            self.output.setText("Congratulations you don't have diabetes.")
        elif self.result == ["Diabetes"]:
            self.output.setText("You have diabetes. Please consult a doctor.")
    
        output_data = {"Date": now.toString(Qt.ISODate), "Name": [Name], "Pregnancies": Pregnancies, "Glucose": Glucose, "Blood Pressure":BloodPressure, "Skin Thickness": SkinThickness, "Insulin": Insulin, "BMI": BMI, "Diabetes Degree Function": DiabetesPedigreeFunction, "Age": Age, "Result": self.result}
        data = pd.DataFrame(output_data)
        #data.to_csv("database.csv")
        with open("database.csv","a") as f:
            data.to_csv(f,header=False,index=False)       
    
    def clear_data(self):
       self.pregnancies.clear()
       self.glucose.clear()
       self.bloodpressure.clear()
       self.skinthickness.clear()
       self.insulin.clear()
       self.bmi.clear()
       self.dpf.clear()
       self.age.clear()
       self.name.clear()
       self.output.setText(" ") 
                       
 

app = QApplication(sys.argv)
window = DiabetesApp()
window.setWindowTitle("Diabetes Check")
window.showMaximized()
app.exec_()