#Vacation via codeacademy.com
city = raw_input("What city would you like to visit? Charlotte, Tampa, Pittsburgh or Los Angeles?")
days = input("How many days would you like to stay?")
spending_money = input("How much spending money would you like to bring?")

def hotel_cost(days):
    return 140 * days

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days >= 7:
        return (days * 40) - 50
    elif days >= 3:
        return (days * 40) - 20
    else:
        return (days * 40)

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost(city, days, spending_money)
