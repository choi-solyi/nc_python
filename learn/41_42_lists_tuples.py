# 4.1 lists

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]


print(days_of_week)

# list.count("Wed") : Wed가 몇개인지 
# list.remove("Mon"): 값 삭제
# list.clear(): 리스트 비우기
# list.reverse(): 순서 뒤집기
# list.append("Sat"): 리스트에 요소 추가하기

# list[n]: n번째 요소 

# modify(수정하다) == mutate(변화시키다)


# 4.2 tuples
# list 와 비슷하지만 더 간단하다!

# list 와 작성법은 동일하지만 대괄호[]가 아닌 소괄호()를 쓴다.
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# tuple은 불변성을 가지며 수정할 수 없다.
# method도 count(), index() 정도만 있다.
# tuple[n] 은 사용할수 있다.
print(days[0])

