import requests

def get_distances_and_times(locations, api_key):
    endpoint = "https://www.mapquestapi.com/directions/v2/routematrix"
  
    params = {
        "key": api_key,
        "locations": locations,
        "outFormat": "json",
        "allToAll": "true"
    }
    response = requests.get(endpoint, params=params)
    data = response.json()

    distances = []
    times = []
    for row in data['distance']:
        for result in row:
            distances.append(result)
    for row in data['time']:
        for result in row:
            times.append(result)
    results = []
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:
                distance = distances[i*len(locations) + j]
                time = times[i*len(locations) + j]
                results.append(f"From {locations[i]} to {locations[j]}: {distance} miles, {time//3600} hours {time%3600//60} minutes")
    return "\n".join(results)


# input("\nPlease type cities: ")
locations = ["New York", "Los Angeles", "Chicago"]
api_key = "myzf3oUjUSCk3Lhn0nfgSHqB4DU4v4CM"
result = get_distances_and_times(locations, api_key)
print(result)