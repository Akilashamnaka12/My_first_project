
menu = {                  #order list
    "burger": 500,
    "pizza": 1200,
    "kottu": 900,
    "fried rice": 1000,
    "sandwich": 300,
    "coke": 150
}


def show_menu():
    print("\n------ MENU ------")
    for food, price in menu.items():
        print(f"{food.title()} - Rs.{price}")
    print("------------------")


def calculate_total(order_list):
    total = 0
    for item in order_list:
        total += menu[item]
    return total


def take_order():
    order_list = []
    
    show_menu()
    
    while True:
        food_name = input("Enter food name (or type 'done' to finish): ").lower()
        
        if food_name == "done":
            break
        
        elif food_name in menu:
            order_list.append(food_name)
            print("Added to order: ")
        
        else:
            print("Sorry! That item is not in the menu.")
    
    if order_list:
        total_bill = calculate_total(order_list)
        
        print("\n------ BILL ------")
        for item in order_list:
            print(f"{item.title()} - Rs.{menu[item]}")
        
        print("------------------")
        print(f"Total Bill: Rs.{total_bill}")
        print("------------------")
    else:
        print("No items ordered.")


# Run the system
take_order()