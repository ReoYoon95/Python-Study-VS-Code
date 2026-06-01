import cv2

# 1. 웹캠 카메라 연결 (오타 수정 필요!)
# 0번은 노트북에 내장된 기본 카메라를 뜻합니다.
cap = cv2.VideoCapture(0)

# 2. 비디오 저장 녹화기 설정
# "myvideo.mp4" 라는 이름으로 저장합니다.
# cv2.VideoWriter_fourcc(*"DIVX"): 영상을 압축할 코덱(Codec)을 지정합니다. (DIVX 형식)
# 20: FPS(초당 프레임 수)를 뜻합니다. 즉, 1초에 20장의 사진을 이어 붙이겠다는 의미입니다.
# (640, 480): 저장할 영상의 화면 해상도 크기(가로 640, 세로 480)입니다.
writer = cv2.VideoWriter(
    "D:\\VS Code File\\python Study\\Python Class Work\\260601\\result_myvideo.mp4",
    cv2.VideoWriter_fourcc(*"DIVX"),
    20,
    (640, 480),
)

# 3. 실시간 영상 처리를 위한 무한 루프 시작
while True:
    # cap.read()는 웹캠에서 실시간으로 '사진 1장'을 가져옵니다.
    # ret: 사진을 정상적으로 가져왔으면 True, 실패했으면 False가 담깁니다.
    # frame: 방금 웹캠이 찍은 '실제 사진 이미지 데이터'가 담깁니다.
    ret, frame = cap.read()

    # 만약 카메라에서 영상을 못 가져왔다면 (예: 카메라가 꺼졌거나 끊김) 안전하게 루프를 빠져나갑니다.
    if not ret:
        break

    # 방금 가져온 사진 1장을 동영상 파일(writer)에 한 칸 추가합니다. (녹화 중)
    writer.write(frame)

    # 방금 가져온 사진 1장을 "frame"이라는 이름의 윈도우 창에 실시간으로 띄웁니다.
    cv2.imshow("frame", frame)

    # 키보드 입력 감지 (오타 수정 필요!)
    # cv2.waitKey(1): 1밀리초(0.001초) 동안 사용자가 키보드를 누르는지 기다립니다.
    # & 0xFF == 27: 누른 키의 아스키 코드가 27(ESC 키)인지 확인합니다.
    # 사용자가 키보드 왼쪽 위의 ESC 키를 누르면 무한 루프를 탈출(break)합니다.
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 4. 마무리 및 자원 반납 (오타 수정 필요!)
cap.release()  # 연결되어 있던 웹캠 카메라를 안전하게 끕니다.
writer.release()  # 녹화 중이던 비디오 파일을 닫고 최종 저장합니다.
cv2.destroyAllWindows()  # 화면에 켜져 있던 "frame" 창들을 모두 닫습니다.
