# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())

entry = {}

for i in range(n):
    text = input().split()
    entry[text[0]] = text[1]
    
while True:
    try:
        name = input()
        if name in entry:
            print(name+"="+entry[name])
        else:
            print("Not found")
    except EOFError:
        break
