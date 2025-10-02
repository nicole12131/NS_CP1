# NS 1st 🔨 Multiplication

print("     ", end="")
for num in range(1, 13):
    print(f"{num:4}", end="")
print()
print("-" * 53)


for i in range(1, 13):
    print(f"{i:3} |", end="")
    for j in range(1, 13):
        result = i * j
        print(f"{result:4}", end="")
    print()