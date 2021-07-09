import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print(x)
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"],["city"],["name"])
