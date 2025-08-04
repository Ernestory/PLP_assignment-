def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Provide values directly
original_price = 200.0
discount_percent = 50.0

# Call the function
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Discount applied! Final price: Kshs{final_price:.2f}")
else:
    print(f"No discount applied. Final price: Kshs {original_price:.2f}")
