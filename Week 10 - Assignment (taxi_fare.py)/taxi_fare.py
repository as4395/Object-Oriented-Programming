"""
The script calculates the taxi fare based on the distance traveled in kilometers.
The base fare is $4.00 and $0.25 is added for every 140 meters traveled. 

"""

def fare_calculator(distance_km):
    if distance_km < 0:
        return None  # Return None when a negative number is the input
    
    base_fare = 4.00
    meters_traveled = distance_km * 1000 
    cost_per_140m = 0.25
    num_segments = meters_traveled / 140  
    
    total_fare = base_fare + (num_segments * cost_per_140m)
    
    return total_fare

def user_input():
    distance = float(input("Enter the distance traveled in kilometers: "))
    
    if distance < 0:
        print("Distance cannot be negative.")
        return
    
    fare = fare_calculator(distance)
    print(f"The total fare for traveling {distance} kilometers is ${fare:.2f}")

user_input()
