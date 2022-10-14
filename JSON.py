# python to json

import json
#python dict
x={
    "name":"raju",
    "age":22,
    "city":"hubli"
}
y=json.dumps(x)
print(y)

# json to python

import json
x='{"name":"arun","age":22, "city":"ckm"}'
y=json.loads(x)
print(y["age"])




import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))