# 4.3 Dicts

# key-value 한쌍

player = {
  'name': 'solyi',
  'age': 33,
  'alive': True,
  'fav_food': ['pizza', 'burger']
}

print(player)
print(player.get('fav_food')) # 
print(player['fav_food'])
player['xp']  = 1500


# dictionary도 여러 method를 가지고 있다.
# dict.clear() # 내용지우기
# dict.get('fav_food') # key를 가지고 value 값 출력하기
# dict['fav_food']  # 위와 동일!
# dict.pop('age') # key를 지운다
# dict['xp']  = 1500 # 새로운 key,value를 추가한다.


# dict 내에 있는  list 에도 똑같이 값을 추가하거나 수정, 삭제 할 수 있다.
print(player['fav_food'][1])
print(player['fav_food'].append('noodles'))
print(player)

# list, tuple과는 쓰임새가 다르다.
# list, tuple 은 to-do list, 숫자 목록 같은 목록을 만들때
# dict 는 많은 속성을 가지고 있는 데이터를 만들때 
