from FindFlights import FindFlights
from flask import Flask, jsonify, request 
from flask_cors import CORS,cross_origin
# 
app = Flask(__name__)
CORS(app)

@app.route("/",methods = ['GET'])
@cross_origin()
def helloWorld():
    data = 200
    return jsonify({'health': data}) 

@app.route("/findFlights",methods = ['POST'])
@cross_origin()
def findFlights():
    try:
        if request.method == 'POST':
            data = request.get_json()
            BookingClass = data.get('BookingClass', "Y") # Process the data (replace this with your actual processing logic)
            TripType=data.get('TripType', "One-Way")
            Travelers=data.get('Travelers', 1)
            data["BookingClass"]=BookingClass
            data["TripType"]=TripType
            data["Travelers"]=Travelers
            data=FindFlights.getflights()
            return jsonify(data)



    except Exception as e:
       
        error_message = f"An error occurred: {str(e)}"
        return error_message, 500 

    data = 200
    return jsonify({'health': data}) 

if __name__ == '__main__': 
    app.run(debug = True) 


