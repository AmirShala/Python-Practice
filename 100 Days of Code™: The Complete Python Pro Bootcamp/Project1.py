"""
Band Name Generator
-------------------

Description:
This script generates a simple band name suggestion based on user input.
It combines the name of the city the user grew up in with their pet's name.

Workflow:
1. Prompts the user to enter:
   - The name of the city they grew up in.
   - Their pet's name.
2. Concatenates both inputs with a space in between.
3. Prints a suggested band name.

Example:
Input:
    City: London
    Pet: Max

Output:
    Your band name could be: London Max
"""


print("Welcome to the Band Name Generator.")
cityName = input("What's the name of the city you grew up in?\n")
petName = input("What's your pet's name?\n")
print("Your band name could be: " + cityName + " " + petName)
