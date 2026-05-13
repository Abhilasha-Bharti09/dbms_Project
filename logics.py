import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Earth radius in kilometers
    R = 6371.0

    # Convert coordinates to radians
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2)**2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return round(distance, 2) # Returns distance in km

# This function filters donors based on distance
def get_nearby_donors(hospital_lat, hospital_lon, donor_list, max_radius_km):
    nearby = []
    for donor in donor_list:
        dist = calculate_distance(hospital_lat, hospital_lon, donor['lat'], donor['lon'])
        if dist <= max_radius_km:
            nearby.append(donor)
    return nearby
def update_request_status(current_status, action):
    """
    Logic: 
    - A 'Pending' request can be 'Accepted'.
    - An 'Accepted' request can be 'Deactivated' (Completed).
    """
    if current_status == "Pending" and action == "accept":
        return "Accepted"
    elif current_status == "Accepted" and action == "completed":
        return "Deactivated"
    else:
        return current_status