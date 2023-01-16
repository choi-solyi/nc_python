# 3.3 And & Or

# input() 입력 받는 function
# int() 값을 숫자로 변경하는 function
age = int(input("How old are you? "))
print("user answer : ", age)

print(type(age)) # class 'str'

if age < 18:
  print("You can't drink!")
elif age >= 18 and age <= 35:
  print("You drink beer!")
elif age == 60 or age == 70:
  print("Birthday party!")
else:
  print("Go ahead!")

# and 를 쓰려면 둘 다 True 여야 한다.
# 하나라도 False 라면 False가 된다.

# or 은 둘중 하나라도 True면 된다


# True and True == True
# False and True == False
# True and False == False
# False and False = False

# True or True == True
# True or False == True
# False or True == True
# False or False == False

# 3.4 Python Standard Library (Built-in function)
# URL : https://docs.python.org/3/library/functions.html

## Python 카지노
from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1, 100) # 1 ~ 100
playing = True
while playing:
  user_choice = int(input("Choose Number! 1-100 "))
  if user_choice == pc_choice:
    print("You Won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")

# Built-in function : 항상 사용할수있는  function

# 그 외에도 function 들도 많이 있는데 import 해서 사용해야한다.
# from random import randint (random int)


# 3.5 While
# 3.4의 코드에 while을 추가한다.

# 주석 : 한줄만 주석 할때는 해쉬태그
"""
 여러줄을 한번에
 주석 처리 하고 싶을 땐
 쌍따옴표 3개

distance = 0
while distance < 20:
  print("I'm running: ", distance, "km")
  distance = distance + 1
"""

# 3.7 Recap
