import numpy as np 
from datetime import datetime

import pickle
model = pickle.load(open('model.pkl', 'rb'))

def preprocessdata(Store, Dept, Date, Temperature, Fuel_Price, MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5, CPI, Unemployment, Size, Type_B, Type_C, IsHoliday_True):
    # Convert inputs to the correct types
    Store = int(Store)
    Dept = int(Dept)
    Date = datetime.strptime(Date, '%Y-%m-%d')
    month_date = Date.month
    day_date = Date.day
    year_date = Date.year
    Temperature = float(Temperature)
    Fuel_Price = float(Fuel_Price)
    MarkDown1 = float(MarkDown1) if MarkDown1 else 0.0
    MarkDown2 = float(MarkDown2) if MarkDown2 else 0.0
    MarkDown3 = float(MarkDown3) if MarkDown3 else 0.0
    MarkDown4 = float(MarkDown4) if MarkDown4 else 0.0
    MarkDown5 = float(MarkDown5) if MarkDown5 else 0.0
    CPI = float(CPI)
    Unemployment = float(Unemployment)
    Size = float(Size)
    Type_B = bool(Type_B)
    Type_C = bool(Type_C)
    IsHoliday_True = bool(IsHoliday_True)

    # Create the test data list
    test_data = [[Store, Dept, Temperature, Fuel_Price, MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5, CPI, Unemployment, Size, month_date, day_date, year_date, Type_B, Type_C, IsHoliday_True]]

    # Make a prediction
    prediction = model.predict(test_data)

    # Format the prediction output
    output = ', '.join(['{0:.2f}'.format(pred) for pred in prediction])

    return output