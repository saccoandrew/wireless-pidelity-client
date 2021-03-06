'''
Created on Nov 18, 2017

@author: saccoa1
'''

'''
#####THE CODE BELOW IS FOR PROOF OF CONCEPT, IN NO WAY RELATED TO THE CODE I NEED######
##Proof of concept for getting json/general json syntax and format
from urllib.request import urlopen
import json
from _multiprocessing import send

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
  
    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print (theJSON["metadata"]["title"])
  
    # output the number of events, plus the magnitude and each event name  
    count = theJSON["metadata"]["count"];
    print (str(count) + " events recorded")
      
    # for each event, print the place where it occurred
    for i in theJSON["features"]:
        print (i["properties"]["place"])

    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

    # print only the events where at least 1 person reported feeling something
    print ("Events that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
    if (feltReports != None):
        if (feltReports > 0):
            print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")
        else:
            feltReports=0
            
  
  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
  
    # Open the URL and read the data
    webUrl = urlopen(urlData)
    print ((webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        # print out our customized results
        printResults(data)
    else:
        print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

if __name__ == "__main__":
    main()

'''
#BELOW IS THE OUTLINE OF JSON STRING DATA THAT WILL BE SENT
def makepin(pin):
    {
    "type": "gpio",
    "op": "make", 
    "pin": "27", 
    "direction": "in"
    }

    
def setpin(pin, value):
    {
    "type": "gpio",
    "op": "set",
    "pin": "27",
    "value": "high"
}