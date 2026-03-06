stack = []
popped = []

n = 10

for i in range(n):
    inp = input("stack push :")
    stack.append(inp)

print("Stack now :", stack)


for i in range (n):
    x = stack.pop()
    popped.append(x)
    print("popped : ",x)

print("poped now : ", popped)

