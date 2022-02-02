"""
Aidan Stout
lab3.py
Problem: creating a program to find the average number of cars that used
    a certain number of roads.
I certify that this lab is entirely my work
"""

def traffic():
    roads = eval(input("How many roads were surveyed?"))
    total_cars = 0
    for i in range(1, roads + 1):
        day_average = 0
        print("How many days was road", i, "surveyed?")
        days = eval(input(""))
        for d in range(1, days + 1):
            print("How many cars traveled on day", d,"?")
            cars = eval(input(""))
            total_cars = total_cars + cars
            day_average = (day_average + cars)
        day_average = day_average / days
        print("Road", i, "average vehicles per day:", round(day_average, 2))
    print("Total number of vehicles travelled on all roads", total_cars)
    road_average = total_cars / roads
    print("Average number of vehicles per road:", round(road_average, 2))
