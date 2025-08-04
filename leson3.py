def large_power(base, exponent):
    result = base ** exponent  # Calculate power
    if result > 5000:
        return True
    else:
        return False

# Test cases
print(large_power(10, 4))   # 10^4 = 10000 → True
print(large_power(2, 8))    # 2^8 = 256 → False
print(large_power(5, 5))    # 5^5 = 3125 → False
print(large_power(8, 5))    # 8^5 = 32768 → True

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
print(divisible_by_ten(20))   # True
print(divisible_by_ten(33))   # False
print(divisible_by_ten(0))    # True
print(divisible_by_ten(100))  # True
print(divisible_by_ten(101))  # False
