d = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "grapefruit": "60",
}

k = input("Item: ").lower()  # You should call the lower() method to convert the input to lowercase

calories = " "

if k in d:
    calories = d[k]
    print(f"Calories: {calories}")
else:
    print("Item not found in the dictionary.")