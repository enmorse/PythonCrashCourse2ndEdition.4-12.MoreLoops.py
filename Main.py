# All versions of foods.py in this section have avoided
# using for loops when printing to save space. Choose
# a version of foods.py, and write two for loops to
# print each list of foods.

my_foods = [
    "steak and eggs",
    "kung pao chicken",
    "carne asada",
]
friends_foods = my_foods[:]

my_foods.append("greek gyros")
friends_foods.append("vegetarian burrito")

my_dinner = f"My favorite foods are:"
friends_dinner = f"My friend's favorite foods are:"

for food in my_foods:
    print(f"{my_dinner}", food.title())

for food in friends_foods:
    print(f"{friends_dinner}", food.title())
