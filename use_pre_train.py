import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True :
    _, frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        
        x1 = face.left()
        y1 = face.top()
        
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0),3)
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x,y),3,(0,255,0),-1)
    cv2.imshow("window", frame)
    if cv2.waitKey(25) & 0XFF == ord('q'):
        break
cv2.destroyAllWindows()

cap.release()