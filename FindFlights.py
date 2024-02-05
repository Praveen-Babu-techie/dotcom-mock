import json

class FindFlights:
  def getflights():
    with open('apidata.json', 'r') as f:
      data = json.load(f)
    return data["data"]["Trips"][0]["Flights"]

