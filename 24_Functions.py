# 2.4 Functions

# function 을 정의할 때 def 를 쓴다.
# 변수와 마찬가지로 숫자로 시작하면 안되고 스네이크 케이스를 쓴다
def say_hello(user_name, user_age): # parameter
  print("hello", user_name, "how r u ?")
  print("you are", user_age, "years old.")


# 2.5 Identation
# python에선 공백이 매우 중요하다. 
# 코드를 두칸 띄워줘야 그 코드가 어떤것 안에 들어가 있는걸 알수있다.

def say_bye():
  print("bye~")

say_bye()

# 2.6 Parameters

# parameter: function의 괄호 안에서 쓰는 인자
# argument: function을 호출할때 쓰는 인자

say_hello("solyi", 33)  # argument
say_hello("louis", 1)
say_hello("may", 1)
say_hello("joy", 1)

# 2.7 Multiple Parameters

# 2.8 Recap
def tex_calculator(money):
  print(money * 0.35)

tex_calculator(1000)

# 2.9 Default Parameters

def say_hello2(user_name="anonymous"):
  print("hello", user_name)

say_hello2("solyi")
say_hello2()

def plus(a=0, b=0):
  print(a + b)

def minus(a=0, b=0):
  print(a - b)

def multiply(a=0, b=0):
  print(a * b)

def devide(a=0, b=1):
  print(a / b)

def powerof(a=0, b=0):
  print(a ** b)

plus(1,2)
minus(3-4)
multiply(1,2)
devide(3,2)
powerof(2,4)

plus()
minus()
multiply()
devide()
powerof()


# 2.10 return values
def tex_calc(money):
  return money * 0.35

def pay_tex(tax):
  print("thank you for paying", tax)

to_pay = tex_calc(15000000)
pay_tex(to_pay)


# 2.10 Return recap
my_name = "solyi"
my_age = 33
my_color_eyes = "black"

print(f"Hello I'm {my_name}, I have {my_age} year in the earth, {my_color_eyes} is my eye color")

def make_juice(fruit):
  return f"{fruit} + 🧃"

def add_ice(juice):
  return f"{juice} + 🧊"

def add_sugar(iced_juice):
  return f"{iced_juice} + 🍬"

juice = make_juice("🍌")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

