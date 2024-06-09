from flask import Flask, render_template, request
import utils
from utils import preprocessdata

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        Store = request.form.get('Store')
        Dept = request.form.get('Dept')
        Date = request.form.get('Date')
        Temperature = request.form.get('Temperature')
        Fuel_Price = request.form.get('Fuel_Price')
        MarkDown1 = request.form.get('MarkDown1')
        MarkDown2 = request.form.get('MarkDown2')
        MarkDown3 = request.form.get('MarkDown3')
        MarkDown4 = request.form.get('MarkDown4')
        MarkDown5 = request.form.get('MarkDown5')
        CPI = request.form.get('CPI')
        Unemployment = request.form.get('Unemployment')
        Size = request.form.get('Size')
        Type_B = request.form.get('Type_B')
        Type_C = request.form.get('Type_C')
        IsHoliday_True = request.form.get('IsHoliday_True')

        # Debugging: print the form values to check if they are being received
        print(f"Received values: Store={Store}, Dept={Dept}, Date={Date}, Temperature={Temperature}, Fuel_Price={Fuel_Price}, MarkDown1={MarkDown1}, MarkDown2={MarkDown2}, MarkDown3={MarkDown3}, MarkDown4={MarkDown4}, MarkDown5={MarkDown5}, CPI={CPI}, Unemployment={Unemployment}, Size={Size}, Type_B={Type_B}, Type_C={Type_C}, IsHoliday_True={IsHoliday_True}")

        # Preprocess the data and get prediction output
        output = utils.preprocessdata(Store, Dept, Date, Temperature, Fuel_Price, MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5, CPI, Unemployment, Size, Type_B, Type_C, IsHoliday_True)

        # Debugging: print the output to check if the prediction is correct
        print(f"Prediction output: {output}")

        return render_template('predict.html', prediction=output)

    return render_template('predict.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
