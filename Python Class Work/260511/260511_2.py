# 연습문제
# 로그인 프로그램 만들기
# -기능
#     -메뉴함수
#         -1. ID,PW 등록
#         -2. 로그인
#         -3. 종료
#     -ID,PW 등록 기능 함수
#         -id_Pass 딕셔너리에 키보드로 부터 입력한 ID와 PW를 암호화 하여 등록 (PW만 암호화)
#     -로그인 기능 함수
#         -키보드로 부터 입력받은 ID, PW를 id_Pass 딕셔너리에서 확인 후 로그인 성능 출력 후 메뉴 출력
#     -종료
#         -메뉴에서 3번을 누르면 프로그램 종료, 그 외 번호를 누르면 무시
#         -로그인 성공 실패시에는 3번을 누르면 무시
# -출력
#     -1. ID, PW등록
#     -2. 로그인
#     -3 종료


def createUserInfo():
    userID = input("ID를 입력하시오 : ")
    userPW = input("PW를 입력하시오 : ")

    encrypted_Pw = encrypt(userPW)

    user_Info[userID] = encrypted_Pw
    print(f"아이디:{userID}, 비밀번호:{userPW}로 회원가입 성공했습니다.")


def encrypt(pw):
    encrypted_Pw = ""  # 암호문
    for c in pw:  # 평문의 모든 글자에 대하여 반복한다.
        x = ord(c)  # 글자의 코드값을 구한다.
        x = x + 1  # 코드값을 하나 증가한다.
        cc = chr(x)  # 증가된 코드값에 해당하는 문자를 계산한다.
        encrypted_Pw += cc  # 암호문에 추가한다.
    return encrypted_Pw


def decrypt(pw):
    plain_pw = ""  # 평문
    for c in pw:  # 암호문의 모든 글자에 대하여 반복한다.
        x = ord(c)  # 글자의 코드값을 구한다.
        x = x - 1  # 코드값을 하나 감소한다.
        cc = chr(x)  # 감소된 코드값에 해당하는 문자를 계산한다.
        plain_pw += cc  # 평문에 추가한다.
    return plain_pw


def LogInInfo():
    while True:
        userID = input("ID를 입력하시오 : ")
        userPW = input("PW를 입력하시오 : ")

        if userID in user_Info.keys():
            if userPW == decrypt(user_Info[userID]):
                print("로그인 성공")
                break
            else:
                print("로그인 실패: 잘못 된 비밀번호")
                continue
        else:
            print("로그인 실패: 잘못된 아이디")
            continue


#     encrypted_text = "Mpwf!xjmm!gjoe!b!xbz/"    # 암호문
# 복호화 코드
# plain_text = ""# 평문
# for c in encrypted_text:    # 암호문의 모든 글자에 대하여 반복한다.
# x = ord(c)  # 글자의 코드값을 구한다.
# X = x - 1   # 코드값을 하나 감소한다.
# cc = chr(x) # 감소된 코드값에 해당하는 문자를 계산한다.
# plain_text = plain_text + cc    # 평문에 추가한다.

# print(plain_text)   # 평문을 출력한다.


user_Info = {}
encrypted_PW_Info = {}  # 원래 비번 : 암호화 비번

while True:
    state = input("회원가입 : 1, 로그인 : 2, 종료 : 3을 입력하시오: ")
    # if state is not 1 or 2 or 3 :
    #     print("잘못된 숫자를 입력하셨습니다. 다시 입력하시오: ")
    #     continue

    match state:
        case "3":
            print("프로그램을 종료합니다")
            break
        case "2":  # 로그인함수
            LogInInfo()
            break
        case "1":  # 회원가입
            createUserInfo()
        case _:
            print("잘못된 숫자를 입력하셨습니다. 다시 입력하시오: ")
            continue


# 암호화

# plain_text="Love will find a way." # 평문

# encrypted_text ="" # 암호문
# for c in plain_text: # 평문의 모든 글자에 대하여 반복한다.
# x = ord(c) # 글자의 코드값을 구한다.
# x = x + 1 # 코드값을 하나 증가한다.
# cc = chr(x) # 증가된 코드값에 해당하는 문자를 계산한다.
# encrypted_text = encrypted_text +cc # 암호문에 추가한다.

# print(encrypted_text) # 암호문을 출력한다.


# encrypted_text = "Mpwf!xjmm!gjoe!b!xbz/"    # 암호문
# 복호화 코드
# plain_text = ""# 평문
# for c in encrypted_text:    # 암호문의 모든 글자에 대하여 반복한다.
# x = ord(c)  # 글자의 코드값을 구한다.
# X = x - 1   # 코드값을 하나 감소한다.
# cc = chr(x) # 감소된 코드값에 해당하는 문자를 계산한다.
# plain_text = plain_text + cc    # 평문에 추가한다.

# print(plain_text)   # 평문을 출력한다.
