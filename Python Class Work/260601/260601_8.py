import cv2

cap = cv2.VideoCapture(0)


writer1 = cv2.VideoWriter(
    "D:\\VS Code File\\python Study\\Python Class Work\\260601\\result_myvideo.mp4",
    cv2.VideoWriter_fourcc(*"DIVX"),
    20,
    (640, 480),
)

while True:

    ret, frame = cap.read()

    writer2 = cv2.stylization(frame, sigma_s=100, sigma_r=0.9)

    writer1.write(writer2)

    cv2.imshow("frame", frame)
    cv2.imshow("Stylized", writer2)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.relase()

writer1.release()

cv2.destroyAllwindows
