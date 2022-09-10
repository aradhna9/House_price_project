import re
from flask import Flask, jsonify,request
import config
from project_data.utils import HousePrice

app = Flask(__name__)


@app.route('/') 
def hello_flask():
    return "INDIA"
    
@app.route('/predict_charges')
def get_house_cost():
    
    data=request.form
       
    crime_rate = eval(data['crime_rate'])
    resid_area = eval(data['resid_area'])
    air_qual = eval(data['air_qual'])
    room_num = eval(data['room_num'])
    age = eval(data['age'])
    dist1 = eval(data['dist1'])
    dist2 = eval(data['dist2'])
    dist3 = eval(data['dist3'])
    dist4 = eval(data['dist4'])
    teachers = eval(data['teachers'])
    poor_prop = eval(data['poor_prop'])
    airport = data['airport']
    n_hot_rooms = eval(data['n_hot_rooms'])
    rainfall = eval(data['rainfall'])
    bus_ter = data['bus_ter']
    parks = eval(data['parks'])
    waterbody = data['waterbody']


    
    price_hs = HousePrice(crime_rate,resid_area,air_qual,room_num,age,dist1,dist2,
                 dist3,dist4,teachers,poor_prop,airport,n_hot_rooms,rainfall,bus_ter,parks,waterbody)
    charges = price_hs.get_predicted_charges()
        
    return jsonify({"Result": f"Predicted house cost are : {charges}"})

    


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)
