Array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

output = []
for i, element in enumerate(Array):
    output.append({"key": i+1, "value": element})

print(output)
