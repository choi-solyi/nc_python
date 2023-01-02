# 3.0 if

# if condition:
#   "write the code to run"

if 10 == 10:
  print("True!!")

a = "solyi"
if a == "solyi":
  print("YES!")

# 3.1 Else & Elif
if 10 > 5:
  print("True")

# else 는 옵션이다 무조건 사용해야하는 것은 아님
password_correct = False # True
if password_correct:
  print("Here is your money.")
else:
  print("Wrong password.")


# elif (== else if)
# else와 마찬가지로 반드시 써야하는것은 아님
winner = 10
if winner > 10:
  print("winner is greater than 10")
elif winner < 10:
  print("Winner is less than 10")
else:
  print("Winner is 10")

# 3.2 Recap

# == 같다
# != 같지않다
# > 크다
# >= 크거나 같다
# < 작다
# <= 작거나 같다

winner2 = 50
if winner2 != 10:
  print("if")
elif winner2 <= 25:
  print("elif")
elif winner2 == 0:
  print("elif 2")
elif winner2 == 50:
  print("elif 3")
else:
  print("else")

# 첫번째 if에서 true이므로 if가 출력된다.
# 뒷부분 조건은 보지 않는다.
