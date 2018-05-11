#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;

int main()
{
	cv::Mat frame, grayImg, edgeImg;
	cv::VideoCapture videoCapture(0);
	if (!videoCapture.isOpened())
	{
		cout << "Error: Unable to initialize webcam!" << endl;
		exit (-1);
	}

	// Create window with trackbars
	int lowThreshold = 50, highThreshold = 150;
	string windowName = "Edge output";
	cv::namedWindow(windowName);
	cv::createTrackbar("Low Threshold", windowName, &lowThreshold, 255);
	cv::createTrackbar("High Threshold", windowName, &highThreshold, 255);

	while(videoCapture.isOpened())
	{
		videoCapture >> frame;

		// Perform canny edge detection
		cv::cvtColor(frame, grayImg, CV_BGR2GRAY);
		Canny(grayImg, edgeImg, lowThreshold, highThreshold);

		cv::imshow("Webcam output", frame);
		cv::imshow(windowName, edgeImg);
		char keyPressed = cv::waitKey(1.0/30.0);

		if (keyPressed == 'q' || keyPressed == 'Q')
		{
			cout << "Program terminated by user!" << endl;
			break;
		}
	}
}