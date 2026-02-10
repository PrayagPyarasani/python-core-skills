nums = list(map(int, input("Enter numbers: ").split()))

evens = list(filter(lambda x: x % 2 == 0, nums))
odds = list(filter(lambda x: x % 2 != 0, nums))

print("Even numbers:", evens)
print("Odd numbers:", odds)
