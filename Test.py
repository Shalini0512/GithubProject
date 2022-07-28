from flask import Flask
import pandas as pd
app = Flask(__name__)


@app.route('/')
def test():  
    jsonStr = '''[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'''
    df = pd.read_json(jsonStr)
    #print(df)

    df['BMI'] = df['WeightKg']/((df['HeightCm']/100)**2)
    category = []
    risk = []
    for row in df['BMI']:
        if row <= 18.4 :
            category.append('Underweight')
            risk.append("Malnutrition risk")
        elif row > 18.4 and row<=24.9:
            category.append('Normal weight')
            risk.append("Low risk")
        elif row > 24.9 and row<=29.9:
            category.append('Overweight')
            risk.append("Enhanced risk")
        elif row > 29.9 and row<=34.9:
            category.append('Moderately obese')
            risk.append("Medium risk")
        elif row > 34.9 and row<=39.9:
            category.append('Severely obese')
            risk.append("High risk")
        else:
            category.append('Very severely obese')
            risk.append("Very high risk")

    df['BMI Category']= category
    df['Health risk']= risk 
    print(df)
    overWeight = df[df['BMI Category']=="Overweight"].shape[0]
    print(overWeight)
    return(overWeight)

if __name__ == '__main__':
    app.run()