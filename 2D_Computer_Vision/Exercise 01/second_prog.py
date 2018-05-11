import cv2

if __name__ == "__main__":
	videoCapture = cv2.VideoCapture(0)
	if not videoCapture.isOpened():
		print ("Error: Unable to initialize webcam!")
		exit (-1)

	while (videoCapture.isOpened()):
		ret, frame = videoCapture.read()
		cv2.imshow("Webcam output", frame)
		keyPressed = cv2.waitKey(1.0/30.0)
		if keyPressed == ord('q') or keyPressed == ord('Q'):
			print ("Program terminated by user!")
			break