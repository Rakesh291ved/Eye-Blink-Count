import cv2 
import dlib 
from scipy.spatial import distance
from imutils import face_utils

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	eye = (A + B) / (2.0 * C)
	return eye

count = 0
total = 0
exit_flag = [False]  # Mutable object for callback

# Button coordinates
btn_start = (10, 50)
btn_end = (110, 90)

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		if btn_start[0] <= x <= btn_end[0] and btn_start[1] <= y <= btn_end[1]:
			exit_flag[0] = True

cv2.namedWindow('Video')
cv2.setMouseCallback('Video', click_event)

while True:
	success, img = cap.read()
	if not success:
		break

	imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = detector(imgGray)

	for face in faces:
		landmarks = predictor(imgGray, face)
		landmarks = face_utils.shape_to_np(landmarks)

		leftEye = landmarks[42:48]
		rightEye = landmarks[36:42]

		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)

		eye = (leftEAR + rightEAR) / 2.0

		if eye < 0.3:
			count += 1
		else:
			if count >= 3:
				total += 1
			count = 0

	cv2.putText(img, f"Blink Count: {total}", (10, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

	# Draw quit button
	cv2.rectangle(img, btn_start, btn_end, (0, 0, 255), -1)
	cv2.putText(img, 'QUIT', (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

	cv2.imshow('Video', img)

	if cv2.waitKey(1) & 0xFF == ord('q') or exit_flag[0]:
		break

cap.release()
cv2.destroyAllWindows()
