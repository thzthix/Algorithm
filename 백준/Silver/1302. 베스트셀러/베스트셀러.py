import sys
input = sys.stdin.readline
books = dict()
N = int(input())
for _ in range(N):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

max_val = max(books.values())
best_sellers = []
for name, value in books.items():
    if value == max_val:
        best_sellers.append(name)
best_sellers.sort()
print(best_sellers[0])