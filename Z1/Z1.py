import math

def max_prime_divisor(n):
    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i

    if n > 2:
        max_prime = n

    return max_prime

def product_of_digits_not_divisible_by_5(n):
    product = 1
    has_valid_digit = False

    for digit in str(abs(n)):
        digit = int(digit)
        if digit % 5 != 0:
            product *= digit
            has_valid_digit = True

    return product if has_valid_digit else 0

def gcd_of_max_odd_composite_divisor_and_digit_product(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    max_odd_composite = -1
    for i in range(3, n + 1, 2):
        if n % i == 0 and not is_prime(i):
            max_odd_composite = i

    if max_odd_composite == -1:
        return None

    digit_product = product_of_digits_not_divisible_by_5(n)
    return math.gcd(max_odd_composite, digit_product)

n = int(input("Введите число: "))
print("Максимальный простой делитель:", max_prime_divisor(n))
print("Произведение цифр, не делящихся на 5:", product_of_digits_not_divisible_by_5(n))
print("НОД максимального нечетного непростого делителя и произведения цифр:",
      gcd_of_max_odd_composite_divisor_and_digit_product(n))




