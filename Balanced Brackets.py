bracket = input()

stack = []


for i in range(len(bracket)):
  if bracket[i]==")":
    if (len(stack)==0):
      stack.append(bracket[i])
    else:
      if(stack[len(stack)-1]=="("):
        stack.pop()
  else:
    stack.append(bracket[i])

if(len(stack)==0):
  print("Balanced")
else:
  print("Non-balanced")
      
    