dict1 = { 'a' : 1 , 'b' : 2}
def inventor(x) : 
    return {a:b for b , a in x.items()}
print(inventor(dict1))