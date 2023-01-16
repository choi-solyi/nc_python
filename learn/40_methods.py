
# 4.0 Methods
# python 에는 3가지 데이터 구조가 있다.

# list
# tuple 
# dictionary

# 자료구조 Data structure란 무엇일까?
# 데이터를 구조화 하고 싶을 때 사용한다.


# list

# days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print(days_of_week)

name = "solyi"
print(name.upper()) # 대문자로 출력
# upper() 외에도 엄 청 많 은 function 들이 결합되어있다.
# "solyi"는 string 인데 내부에 많은 function 을 가지고 있다.
# 이것들을 function 이 아닌 method 라고 부른다.

# capitalize: 첫 문자를 대문자로
print(name.capitalize()) 
##  capitalize() 만으로는 사용할 수 없다. string 안에 capitalize 라는 method가 있다.

# replace: a 를 b로 바꾼다
print(name.replace('o','l')) 

# startwith: s로 시작하는지 체크 결과는 bool
print(name.startswith("s")) 

# 위에 있는것들을 method라고 한다.

# 참고url: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str


# method: 데이터와 결합되어 있을때
# function: 그렇지 않을때

