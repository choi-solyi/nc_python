# 2.0 Hello world
print("Hello world!")

# 2.1 Variables 변수
a = 2
b = 3
c = a + b
c = 1 #파이썬은 위에서 아래로 코드를 읽는다.
print(c)

# 변수는 숫자나 기호가 아닌 글자로 시작 해야한다.
# 변수명에는 띄어쓰기를 사용할 수 없다.
# python에서는 스네이크 케이스로 작성한다.

myAge = 77  # camelCase는 javascript에서 많이 사용된다.
my_age = 77 # python 에서는 스네이크 케이스를 많이 쓴다.
print(myAge)
print(my_age)

# 2.2 Booleans and Strings 
my_name = "solyi"
print(my_name)


# True, False 는 첫 글자를 대문자로 작성한다
isTrue = True
isFalse = False
print(isTrue)
print(isFalse)

# 2.3 Recap
my_name2 = "solyi"
my_age2 = "33"
dead = False

print("Hello My name is ", my_name2)
print("and I'm ", my_age2, " years old.")