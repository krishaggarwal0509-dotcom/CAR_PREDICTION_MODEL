from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open("LinearRegressionModel.pkl",'rb'))
car=pd.read_csv('Cleaned Car.csv')

@app.route('/')

def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=sorted(car['fuel_type'].unique())
    return render_template('index.html',companies=companies,car_models=car_models,year=year,fuel_type=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    car_models = request.form.get('car_model')
    kms_driven=int(request.form.get('kilo_driven'))

    prediction = model.predict(pd.DataFrame(
        [[car_models, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    ))

    return str(prediction[0])
if __name__ == '__main__':
    app.run(debug=True)