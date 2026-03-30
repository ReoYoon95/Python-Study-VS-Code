# 문제
# 친구들의 리스트 생성하기
#     가장 친한 친구 5명의 이름을 리스트에 저장했다가 출려하는 프로그램 작성
# 조건
#     키보드로 부터 5명의 이름을 입력 받아 리스트에 저장
#     in 명령어를 이용해서 키보드로 부터 입력 받은 친구가 있는지 확인
#     키보드로 부터 입력 받은 index번호를 가지고 친구의 이름을 출력한다.
#     또 키보드로 부터 입력 받은 이름하고 위에서 입력 받은 인덱스 번호를 이용하여 친구 이름 변경


name_list = []
name_list.append(input("1번째 친구 이름 입력: "))
name_list.append(input("2번째 친구 이름 입력: "))
name_list.append(input("3번째 친구 이름 입력: "))
name_list.append(input("4번째 친구 이름 입력: "))
name_list.append(input("5번째 친구 이름 입력: "))
# list(map(str, input("이름을 한칸씩 띄어서 입력하시오: ").split()))

print(input("친구확인 : (이름입력)") in name_list)
print(name_list[int(input("인덱스번호 이름 확인 : (숫자입력)"))])

name_list[int(input("바꾸고 싶은 인덱스 번호 입력: "))] = str(input("바꿀 이름 입력: "))
print({name_list[int(input("확인하고 싶은 인덱스 번호 입력"))]})
