NUM = 8
nums = []
total = 0

for i in range(NUM):
    num = int(input("Por favor, introduzca el número: "))
    nums.append(num)
    total += num

print("El total de números es:", total)
