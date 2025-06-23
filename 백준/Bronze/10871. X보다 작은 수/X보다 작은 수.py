a,b = map(int, input().split())
numbers = input().split()
print(" ".join(n for n in numbers if int(n)<b))