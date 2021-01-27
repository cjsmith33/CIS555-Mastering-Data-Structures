"""
Module to demonstrate functions on nested dictionaries.

This module uses the data in the file 'weather.json'.  This module does not need to
worry about reading and opening the file -- test.py does that.  However, you should
look at that file to familiarize your self with the data format.

In that file weather is a dictionary whose keys are timestamps (year,month,day,hour,etc.)
and whose values are weather reports.  For example, here is an example of a
(small portion of) a weather dictionary:

    {
        "2017-04-21T08:00:00-04:00": {
            "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 13.9,
                "units": "C"
            },
            "sky": [
                {
                    "cover": "clouds",
                    "type": "broken",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704211056Z"
        },
        "2017-04-21T07:00:00-04:00": {
            "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 57.0,
                "units": "F"
            },
            "sky": [
                {
                    "type": "overcast",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704210956Z"
        }
        ...
    },

The contents of interest in this module is the nested "temperature" dictionary.

IMPORTANT: Not all weather reports contain a temperature measurement.

Author: Charles Smith
Date: 25 January 2021
"""


# Helper to use in function below
def to_celsius(x):
    """
    Returns x converted to celsius

    The value returned has type float.

    Parameter x: the temperature in fahrenheit
    Precondition: x is a number
    """
    return 5*(x-32)/9.0


# Implement this function
def reports_above_temp(weather,temp):
    """
    Returns the number of weather reports where temperature is above temp (in Celsius)

    The parameter weather contains a weather report dictionary.  This function loops
    through the weather reports and counts all reports for which
    (1) the report has a temperature measurement (not all reports do)
    (2) the measured temperature is properly above temp in Celsius

    A temperature measurement is itself a dictionary with two keys: 'value' and 'units'.
    For example:

        "temperature": {
            "value": 57.0,
            "units": "F"
        }

    The units are always either 'F' for fahrenheit or 'C' for celsius.  If the
    measurement is in fahrenheit, the value will need to be converted before it
    can be compared to temp.

    Parameter weather: the weather dictionary
    Precondition: weather has the format described in the module introduction

    Parameter temp: the temperature in celsius
    Precondition: temp is a float
    """
    retVal = 0
    value = 0

    for key1 in weather.keys():
        for key2 in weather[key1].keys():
            if str('temperature') in key2:
                for k,v in weather[key1][key2].items():
                    value = weather[key1][key2]['value']
                    if v == str('F'):
                        value = to_celsius(value)
                if value > temp:
                    retVal+=1
    return retVal
