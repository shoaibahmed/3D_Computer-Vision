import cv2

lowThreshold = 50
highThreshold = 150

def onTrackbarChangedLowThresh(val, *params):
	global lowThreshold
	lowThreshold = val
	print ("Low threshold: %d" % lowThreshold)

def onTrackbarChangedHighThresh(val, *params):
	global highThreshold
	highThreshold = val
	print ("High threshold: %d" % highThreshold)

if __name__ == "__main__":
	fps = 30
	delay = int(1000 / fps)
	videoCapture = cv2.VideoCapture(0)
	if not videoCapture.isOpened():
		print ("Error: Unable to initialize webcam!")
		exit (-1)

	# Create window with trackbars
	windowName = "Edge output"
	cv2.namedWindow(windowName)
	cv2.createTrackbar("Low Threshold", windowName, lowThreshold, 255, onTrackbarChangedLowThresh)
	cv2.createTrackbar("High Threshold", windowName, highThreshold, 255, onTrackbarChangedHighThresh)

	while (videoCapture.isOpened()):
		ret, frame = videoCapture.read()

		# Perform canny edge detection
		grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		edgeImg = cv2.Canny(grayImg, lowThreshold, highThreshold)

		cv2.imshow("Webcam output", frame)
		cv2.imshow(windowName, edgeImg)
		keyPressed = cv2.waitKey(delay)
		if keyPressed == ord('q') or keyPressed == ord('Q'):
			print ("Program terminated by user!")
			break
