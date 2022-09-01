exit = True
while exit:
  a = int(input("Choose a number:\n"))
  b = int(input("Choose another one:\n"))
  c = input("""Choose an operation: \n
        Options are : + , - , * or /.
        Write 'exit' to finish\n""")
  if c == 'exit':
    exit == False
  elif c == '+':
    print("Result: ",a+b)
  elif c =='-':
    print("Result: ",a-b)
  elif c == '*':
    print("Result: ",a*b)
  elif c == '/':
    print("Result: ",a/b)