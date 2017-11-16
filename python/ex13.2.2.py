# Ex13.2

from sys import argv
script, car_make, car_model = argv

print("Ordered car make is: ", car_make)
print(f"Unfortunately, {car_model} is currently unavailable.")

car_model_alt = input("Would you like to choose a different model?")

# going a bit ahaid, we ask user to input alternative argument, which is tested in if statement and depending on user input, it gives appropriate answer
if car_model_alt == 'S60' or car_model_alt == 'S80' or car_model_alt == 'XC60':
    print(f"We are happy to confirm that {car_model_alt} is currently in stock and can be modified to your liking before order")
else:
    print(f"Unfortunately, {car_model_alt} is also unavailable.")
