import sys

while True:
    try: 
        line = input()
        print(line.strip())
    except EOFError:
        break