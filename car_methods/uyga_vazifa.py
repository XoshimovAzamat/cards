import os
from data import create_data
import json


def add_cars():
    cars = {}
    while True:
        status = input("Ma`lumot qo`shish uchun: 1 \nMa`lumotlarni o`qish uchun: 2\
         \nMoshina o`chirish uchun: 3  \nMa`lumotlarni tahrirlash uchun: 4\
         \nDasturni tugatish uchun: 0 ")
        if status == "1":

            if os.path.exists("cars.json"):
                try:
                    cars = create_data(None, "cars.json", 'r')
                    print(cars)
                except:
                    print("error")

            name_car = str(input("Moshina nomini kiriting: "))
            color = str(input("Rangi: "))
            price = int(input("Narx: "))

            cars[name_car] = {
                'Rangi': color,
                'Narxi': price
            }
            create_data(cars, "cars.json", "w")

        if status == "3":
            if os.path.exists("cars.json"):
                cars = create_data(None, "cars.json", 'r')
            deleet = input("O`chirmoqchi bo`lgan moshina nomi: ")
            cars.pop(deleet)
            create_data(cars, "cars.json", "w")
            print("\nO`chirildi.")

        if status == "2":
            print()
            print(create_data(cars, "cars.json", 'r'))
            print()
        if status == "4":
            cars = create_data(None,  "cars.json", "r")
            edit = input("Tahrirlamoqchi bo`lgan ma`lumotingiz: ")
            edit2 = input(f"'{edit}'ning qaysi biri o`zgarsin: ")
            new_edit = input("Qanday o`zgarsin: ")
            cars[edit][edit2] = new_edit
            create_data(cars, "cars.json", 'w')

        if status == "0":
            print("\nDastur yakunlandi.")
            break


add_cars()
