import cv2

# 1. 원본 이미지 불러오기
# cv2.IMREAD_COLOR 옵션으로 국수 사진을 '컬러' 상태 그대로 읽어옵니다.
img1 = cv2.imread(
    "D:\\VS Code File\\python Study\\Python Class Work\\260601\\noddle.jpg",
    cv2.IMREAD_COLOR,
)

# 2. 스타일화(수채화/유화 느낌) 필터 적용하기
# sigma_s(공간 대역폭): 값이 클수록 부드러워지고, 스케치 느낌이 강해집니다 (0~200)
# sigma_r(범위 대역폭): 값이 클수록 색상이 뭉개지면서 단순해집니다 (0~1)
img2 = cv2.stylization(img1, sigma_s=100, sigma_r=0.9)

# 3. 화면에 결과 띄우기
cv2.imshow("original", img1)  # "original"이라는 창에 원본 사진 띄우기
cv2.imshow("result", img2)  # "result"라는 창에 필터가 적용된 사진 띄우기

# 4. 키보드 입력 대기 및 창 닫기
cv2.waitKey(0)  # 사용자가 키보드 아무 키나 누를 때까지 창을 닫지 않고 무한 대기합니다.
cv2.destroyAllWindows()  # 키를 누르면 열려 있던 모든 이미지 창을 깔끔하게 닫습니다.

# 5. 이미지 파일로 저장하기
cv2.imwrite(
    "D:\\VS Code File\\python Study\\Python Class Work\\260601\\result_noddle.jpg",
    img2,
) # 필터가 적용된 img2 변수를 "result.jpg"라는 이름으로 저장합니다.
