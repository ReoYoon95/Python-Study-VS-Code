prices = [1000, 2500, 5000]

# 모든 가격에 10% 부가세를 더하고 싶을 때
# map(함수, 리스트) -> 모든 요소에 함수를 적용함
tax_included = list(map(lambda p: int(p * 1.1), prices))

print(tax_included)  # [1100, 2750, 5500]


# 위의 코드를 def식으로 변경
def reprice(a):
    return a * 1.1


# 위의 코드를 람다사용으로 변경
reprice1 = list(map(lambda p: int(p * 1.1), prices))





score_dict = {'Math': 90, 'Science': 85, 'English': 100}

# 딕셔너리의 items()는 (키, 값) 튜플을 줍니다.
# 값을 기준으로 정렬하고 싶다면 x[1]을 기준으로!
sorted_scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

print(sorted_scores) # [('English', 100), ('Math', 90), ('Science', 85)]