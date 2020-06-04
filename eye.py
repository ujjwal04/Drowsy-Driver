import cv2

import time
import winsound


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# img = cv2.imread('lena.jpg')

cap = cv2.VideoCapture(0)
blinks = 0
start_time = time.time()


while cap.isOpened():
    _, img = cap.read()

    img = cv2.resize(img, None, fx=1.5, fy=1.5)

    text = "BLINKS: " + str(blinks)
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, text, (10, 50), font, 1,
                      (0, 255, 255), 2, cv2.LINE_AA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[x:x+w, y:y+h]
        roi_color = img[x:x+w, y:y+h]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 2)
        print(len(eyes))
        if len(eyes) != 0:
            print(start_time)
            print("Okay")
            for (ex, ey, ew, eh) in eyes:
                rect = cv2.rectangle(roi_color, (ex, ey),
                                     (ex+ew, ey+eh), (0, 255, 0), 5)
        else:
            end_time = time.time()
            print(end_time-start_time)

            if end_time-start_time > 3:
                print("Danger")
                print(end_time-start_time)
                frequency = 2500
                duration = 1000
                winsound.Beep(frequency, duration)
                start_time = time.time()
                blinks += 1

    cv2.imshow("IMAGE", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
