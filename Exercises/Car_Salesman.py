base_price = int(input("Please enter the base price of car: "))

tax = base_price * 20/100

license = base_price * 5/100

final_price = base_price + tax + license + 100 + 500

print(f'The final price is: {final_price}')