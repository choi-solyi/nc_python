playing = True

# add your code here!
while playing:
  
  a = int(input("Choose a number:\n"))
  b = int(input("Choose another one:\n"))
  operation = input("Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n")

  if operation == "exit":
    playing = False
  elif operation == "+":
    result = a + b
    print("Result:", result)
  elif operation == "-":
    result = a - b
    print("Result:", result)
  elif operation == "*":
    result = a * b
    print("Result:", result)
  elif operation == "/":
    if b == 0:
      print("It cannot be divided by zero.")
    else:
      result = a / b
      print("Result:", result)