# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 18:09:05 2025

@author: carpa
"""
# jc_midterm.py
# Author: Jessica Carpanini
# Course: INF308

#Write a program that helps a user create and manage a grocery shopping list. 

#add items to the shopping list
def add_item(shopping_list):
    item = input("Add item to your shopping list: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.\n")
        
#remove item from the shopping list
def remove_item(shopping_list):
    item = input("Remove item to your shopping list: ")
    if item in shopping_list: 
        shopping_list.remove(item)
        print(f"{item} has been removed to your shopping list.\n")
    else:
        print(f"{item} is not on your shopping list.\n")

#display the shopping list
def display_list(shopping_list):
    if shopping_list:
        print("\nYour shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("\nYour shopping list is currently empty.")
    print()
    
# Main
def main():
    # Initialize an empty shopping list
    shopping_list = []  
    while True:
        # Menu options
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View the list")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            display_list(shopping_list)
        elif choice == "4":
            print("Goodbye! Have a great day.")
            # Exit the program
            break  
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()   