import json
x = '{"name":"Sarvin","lastname":"Nami","isMarried":false,"age":20,"city":"Tehran","gender":"female","favorites":null}'
y = json.loads(x)
print(x)
print(y)
w = json.dumps(y)
print(w)