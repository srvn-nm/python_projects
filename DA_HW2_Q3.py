n = int(input())
c = int(input())
lightsStatus = ["1"] * n
OnIndexes = input().split(" ")
OnIndexes.remove(OnIndexes[len(OnIndexes) - 1])
OffIndexes = input().split(" ")
OffIndexes.remove(OffIndexes[len(OffIndexes) - 1])