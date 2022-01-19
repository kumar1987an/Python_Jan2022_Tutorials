<<<<<<< HEAD
x = 45.78
print(x * 7388)
print("Python")


# Indentation = 4 spaces = 1 tab space

# Loops
for value in [1, 2, 3, 4, 5]:
    print(value + 2)


# Condition Checks
print("The Leap years are ")
for value in range(2000, 2010): # Indentation Level1
    if value % 4 == 0: # Indentation Level2
        print(value)
        if value % 3 == 0: # Indentation Level3
            print(value)



# Function definitions
def addition_of_numbers(x, y):
    return x + y

print("Addition of two numbers is ",addition_of_numbers(8, 6))


# Class definitions
class Species:
    pass # skip the code block without executing it


# Error Exceptions and Handling
try:
    pass
except:
    pass
else:
    pass
finally:
    pass


# with context manager
with open("log100.txt", "w") as file:
    file.write("Hello World")
=======
>>>>>>> origin/main
