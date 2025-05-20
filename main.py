import sys



""" x = ["apple", "banana", "cherry"]
y = enumerate(x)

for i, valor in y:
    print(f"la posición es : {i}-- y el valor es : {valor}") """


""" list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = zip(list1, list2)
print(list(zipped)) """

"""explicación de como funciona sys"""
if len(sys.argv) > 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])

print(f"el número pasado por parámetro es : {num1}, {num2}, {num3}")

