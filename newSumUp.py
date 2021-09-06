def sumUp(x) :
    if x == 0 : return 0
    else: return sumUp(x-1) + x
print(f'\nthis is the sum up of your range : {sumUp(int(input("please enter the end of your range here : ")))}\n')