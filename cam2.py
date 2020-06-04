import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))

cap.set(3, 1280)
cap.set(4, 720)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font,
                            1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Camera Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
