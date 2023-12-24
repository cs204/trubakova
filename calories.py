fruit = input("Фрукт: ")
fruits = {
    "Apple": 130,
    "Banana": 96,
    "Orange": 62,
    "Strawberries": 32,
    "Grapes": 69,
    "Watermelon": 30,
    "Pineapple": 50,
    "Mango": 60,
    "Pear": 102,
    "Cherry": 50,
    "Peach": 38,
    "Blueberries": 57,
    "Raspberries": 53,
    "Blackberries": 62,
    "Kiwi": 41,
    "Pomegranate": 83,
    "Avocado": 50,
    "Lemon": 29,
    "Lime": 20,
    "Plum": 46
}
if fruit in fruits:
    calories = fruits[fruit]
    print(f"Калории: {calories}")