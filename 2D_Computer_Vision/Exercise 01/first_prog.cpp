#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;

int main()
{
	cv::Mat frame;
	cv::VideoCapture videoCapture(0);
	if (!videoCapture.isOpened())
	{
		cout << "Error: Unable to initialize webcam!" << endl;
		exit (-1);
	}

	videoCapture >> frame;
	while(!frame.empty())
	{
		cv::imshow("Webcam output", frame);
		videoCapture >> frame;
		char keyPressed = cv::waitKey(1.0/30.0);
		if (keyPressed == 'q' || keyPressed == 'Q')
		{
			cout << "Program terminated by user!" << endl;
			break;
		}
	}
}