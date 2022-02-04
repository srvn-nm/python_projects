import keyboard
choice = []
list1 = []
choice.append(keyboard.record(until = 'Esc').split())
mapObj = map(int, choice)
list1.append(list(mapObj))
print (list1)