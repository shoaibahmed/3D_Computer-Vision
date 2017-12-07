import os, sys
import numpy as np
import cv2 as cv

import scipy.io as io


def project_points(X, K, R, T, distortion_flag=False, distortion_params=None):
        """
        Your implementation goes here!
        """
        # Project points from 3d world coordinates to 2d image coordinates
        X_camera = np.matmul(R, X) + T
        X_camera = X_camera / X_camera[2, :] # Normalize

        if distortion_flag:
            radiusSq = (X_camera[0, :] * X_camera[0, :]) + (X_camera[1, :] * X_camera[1, :])
            X_camera = X_camera * (1 + (distortion_params[0] * radiusSq) + (distortion_params[1] * (radiusSq * radiusSq)) + (distortion_params[4] * (radiusSq * radiusSq * radiusSq)))
            # X_camera = (X_camera * (1 + (distortion_params[0] * radiusSq) + (distortion_params[1] * (radiusSq * radiusSq)) + (distortion_params[4] * (radiusSq * radiusSq * radiusSq)))
            #                 + (2 * distortion_params[2] * X_camera[0,:] * X_camera[1,:]) + distortion_params[3] * (radiusSq + (2 * X_camera * X_camera)))

        X_camera[2, :] = 1.0
        X_camera = np.matmul(K, X_camera)
        X_camera = X_camera[:2, :]

        return X_camera

def project_and_draw(out_name, imgOrig, X_3d, K, R, T, distortion_flag, distortion_parameters):
    """
        Your implementation goes here!
    """
    # call your "project_points" function to project 3D points to camera coordinates
    cameraCoords = project_points(X_3d, K, R, T, distortion_flag, distortion_parameters)
    img = imgOrig.copy()

    # draw the projected points on the image and save your output image here
    for i in range(cameraCoords.shape[1]):
        currentPoint = cameraCoords[:, i]
        currentPoint = currentPoint.astype(int)
        if distortion_flag:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
        cv.circle(img, tuple(currentPoint.tolist()), 3, color, -1)
    cv.imwrite(out_name, img)

    return True

if __name__ == '__main__':
    base_folder = './data/'

    image_num = 1
    data = io.loadmat('./data/ex1.mat')
    X_3D = data['X_3D'][0]
    TVecs = data['TVecs']       # Translation vector: as the world origin is seen from the camera coordinates
    RMats = data['RMats']       # Rotation matrices: converts coordinates from world to camera
    kc = data['dist_params']    # Distortion parameters
    Kintr = data['intinsic_matrix'] # K matrix of the cameras
    
    imgs = [cv.imread(base_folder+str(i).zfill(5)+'.jpg') for i in range(TVecs.shape[0])]

    project_and_draw("out.png", imgs[image_num], X_3D, Kintr, RMats[image_num], TVecs[image_num], False, kc)
    project_and_draw("out-radial.png", imgs[image_num], X_3D, Kintr, RMats[image_num], TVecs[image_num], True, kc)