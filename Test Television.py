# Kristine Joy Barrina #BSCPE 1-5 # May 13, 2023
# Create a Python Code for creating the Class and a Test Driver program that will create two objects and produce output.

# Import Class Television to Test Television program
from Television import Television
from colorama import Style, Back, Fore

# Create two objects
television1 = Television(1, 30, 3, 1)
television2 = Television(2, 3, 2, 1)

# Call all methods and print their function
# Display it through using colorama

print ("\n", Fore.GREEN, Back.BLACK, television1.show_name(), television1.get_channel(), "and", television1.get_volume(), Style.RESET_ALL, "\n")
print ("\n", Fore.GREEN, Back.BLACK, television2.show_name(), television2.get_channel(), "and", television2.get_volume(), Style.RESET_ALL, "\n")
