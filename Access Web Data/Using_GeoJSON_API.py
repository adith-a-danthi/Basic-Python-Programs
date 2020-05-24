"""
To complete this assignment, you should use this API endpoint that has a static
subset of the Google Data:
http://python-data.dr-chuck.net/geojson

This API uses the same parameters (sensor and address) as the Google API. This
API also has no rate limit so you can test as often as you like. If you visit
the URL with no parameters, you get a list of all of the address values which
can be used with this API.

To call the API, you need to provide a sensor=false parameter and the address
that you are requesting as the address= parameter that is properly URL encoded
using the urllib.urlencode() fuction as shown in
http://www.pythonlearn.com/code/geojson.py

TEST DATA / SAMPLE EXECUTION
You can test to see if your program is working with a location of "South Federal
University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".
"""

"""
JSON Response
{
  "results": [
    {
      "access_points": [],
      "address_components": [
        {
          "long_name": "#300",
          "short_name": "#300",
          "types": [
            "subpremise"
          ]
        },
        {
          "long_name": "4001",
          "short_name": "4001",
          "types": [
            "street_number"
          ]
        },
        {
          "long_name": "700 East",
          "short_name": "700 E",
          "types": [
            "route"
          ]
        },
        {
          "long_name": "Salt Lake City",
          "short_name": "Salt Lake City",
          "types": [
            "locality",
            "political"
          ]
        },
        {
          "long_name": "Salt Lake County",
          "short_name": "Salt Lake County",
          "types": [
            "administrative_area_level_2",
            "political"
          ]
        },
        {
          "long_name": "Utah",
          "short_name": "UT",
          "types": [
            "administrative_area_level_1",
            "political"
          ]
        },
        {
          "long_name": "United States",
          "short_name": "US",
          "types": [
            "country",
            "political"
          ]
        },
        {
          "long_name": "84107",
          "short_name": "84107",
          "types": [
            "postal_code"
          ]
        }
      ],
      "formatted_address": "4001 700 E #300, Salt Lake City, UT 84107, USA",
      "geometry": {
        "location": {
          "lat": 40.6849285,
          "lng": -111.8700525
        },
        "location_type": "ROOFTOP",
        "viewport": {
          "northeast": {
            "lat": 40.68627748029149,
            "lng": -111.8687035197085
          },
          "southwest": {
            "lat": 40.6835795197085,
            "lng": -111.8714014802915
          }
        }
      },
      "place_id": "ChIJBVZvCm6KUocRoh4bYfH-h2M",
      "plus_code": {
        "compound_code": "M4MH+XX Salt Lake City, Utah, United States",
        "global_code": "85GCM4MH+XX"
      },
      "types": [
        "establishment",
        "point_of_interest",
        "university"
      ]
    }
  ],
  "status": "OK"
}
"""

import urllib.request as ur
import urllib.parse as up
import json

service_url = "http://py4e-data.dr-chuck.net/json?"

address_input = input("Enter location: ")
params = {"sensor": "false", "address": address_input, "key": 42}
url = service_url + up.urlencode(params)

print("Receiving:", url)
data = ur.urlopen(url).read()
print("Retrieved", len(data), "characters")
json_obj = json.loads(data)
place_id = json_obj["results"][0]["place_id"]
print("Place ID:", place_id)
