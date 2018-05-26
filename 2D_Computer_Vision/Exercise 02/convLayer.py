import numpy as np

def conv_forward_naive_correct(x, w, b, conv_param):
  """
  A naive implementation of the forward pass for a convolutional layer.

  The input consists of N data points, each with C channels, height H and width
  W. We convolve each input with F different filters, where each filter spans
  all C channels and has height HH and width HH.

  Input:
  - x: Input data of shape (N, C, H, W)
  - w: Filter weights of shape (F, C, HH, WW)
  - b: Biases, of shape (F,)
  - conv_param: A dictionary with the following keys:
    - 'stride': The number of pixels between adjacent receptive fields in the
      horizontal and vertical directions.
    - 'pad': The number of pixels that will be used to zero-pad the input.

  Returns a tuple of:
  - out: Output data, of shape (N, F, H', W') where H' and W' are given by
    H' = 1 + (H + 2 * pad - HH) / stride
    W' = 1 + (W + 2 * pad - WW) / stride
  - cache: (x, w, b, conv_param)
  """
  outShape = (int(1 + (x.shape[2] + 2 * conv_param['pad'] - w.shape[2]) / conv_param['stride']), \
              int(1 + (x.shape[3] + 2 * conv_param['pad'] - w.shape[3]) / conv_param['stride']))
  out = np.zeros((x.shape[0], w.shape[0], outShape[0], outShape[1]))
  #############################################################################
  # TODO: Implement the convolutional forward pass.                           #
  # Hint: you can use the function np.pad for padding.                        #
  #############################################################################
  x = np.pad(x, [(0, 0), (0, 0), (conv_param['pad'], conv_param['pad']), (conv_param['pad'], conv_param['pad'])], 'constant')
  k_H = int(np.floor(w.shape[2] / 2.0))
  k_W = int(np.floor(w.shape[3] / 2.0))
  print ("K_H: %d | K_W: %d" % (k_H, k_W))
  for inputIter in range(x.shape[0]):
    for filterIter in range(w.shape[0]):
      # for i in range(conv_param['pad'], x.shape[2] + conv_param['pad'], conv_param['stride']):
      #   for j in range(conv_param['pad'], x.shape[3] + conv_param['pad'], conv_param['stride']):
      hIter = k_H
      for i in range(out.shape[2]):
        wIter = k_W
        for j in range(out.shape[2]):
          print ("Shape: %s" % str(list(range(hIter-k_H,hIter+k_H+1))))
          print ("Cropped input shape: %s" % str(x[inputIter, :, hIter-k_H:hIter+k_H, wIter-k_W:wIter+k_W].shape))
          print ("Cropped filter shape: %s" % str(w[filterIter, :, :, :].shape))
          out[inputIter, filterIter, i, j] = np.sum(np.multiply(x[inputIter, :, hIter-k_H:hIter+k_H, wIter-k_W:wIter+k_W], w[filterIter, :, :, :])) + b[filterIter]
          wIter += conv_param['stride']
        hIter += conv_param['stride']
   
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################
  cache = (x, w, b, conv_param)
  return out, cache

def conv_forward_naive(x, w, b, conv_param):
  """
  A naive implementation of the forward pass for a convolutional layer.

  The input consists of N data points, each with C channels, height H and width
  W. We convolve each input with F different filters, where each filter spans
  all C channels and has height HH and width HH.

  Input:
  - x: Input data of shape (N, C, H, W)
  - w: Filter weights of shape (F, C, HH, WW)
  - b: Biases, of shape (F,)
  - conv_param: A dictionary with the following keys:
    - 'stride': The number of pixels between adjacent receptive fields in the
      horizontal and vertical directions.
    - 'pad': The number of pixels that will be used to zero-pad the input.

  Returns a tuple of:
  - out: Output data, of shape (N, F, H', W') where H' and W' are given by
    H' = 1 + (H + 2 * pad - HH) / stride
    W' = 1 + (W + 2 * pad - WW) / stride
  - cache: (x, w, b, conv_param)
  """
  outShape = (int(1 + (x.shape[2] + 2 * conv_param['pad'] - w.shape[2]) / conv_param['stride']), \
              int(1 + (x.shape[3] + 2 * conv_param['pad'] - w.shape[3]) / conv_param['stride']))
  out = np.zeros((x.shape[0], w.shape[0], outShape[0], outShape[1]))
  #############################################################################
  # TODO: Implement the convolutional forward pass.                           #
  # Hint: you can use the function np.pad for padding.                        #
  #############################################################################
  x = np.pad(x, [(0, 0), (0, 0), (conv_param['pad'], conv_param['pad']), (conv_param['pad'], conv_param['pad'])], 'constant')
  for inputIter in range(x.shape[0]):
    for filterIter in range(w.shape[0]):
      hIter = 0
      for i in range(out.shape[2]):
        wIter = 0
        for j in range(out.shape[2]):
          out[inputIter, filterIter, i, j] = np.sum(np.multiply(x[inputIter, :, hIter:hIter+w.shape[2], wIter:wIter+w.shape[3]], w[filterIter, :, :, :])) + b[filterIter]
          wIter += conv_param['stride']
        hIter += conv_param['stride']
   
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################
  cache = (x, w, b, conv_param)
  return out, cache

x_shape = (2, 3, 4, 4)
w_shape = (3, 3, 4, 4)
x = np.linspace(-0.1, 0.5, num=np.prod(x_shape)).reshape(x_shape)
w = np.linspace(-0.2, 0.3, num=np.prod(w_shape)).reshape(w_shape)
b = np.linspace(-0.1, 0.2, num=3)

conv_param = {'stride': 2, 'pad': 1}
out, _ = conv_forward_naive(x, w, b, conv_param)
correct_out = np.array([[[[-0.08759809, -0.10987781],
                           [-0.18387192, -0.2109216 ]],
                          [[ 0.21027089,  0.21661097],
                           [ 0.22847626,  0.23004637]],
                          [[ 0.50813986,  0.54309974],
                           [ 0.64082444,  0.67101435]]],
                         [[[-0.98053589, -1.03143541],
                           [-1.19128892, -1.24695841]],
                          [[ 0.69108355,  0.66880383],
                           [ 0.59480972,  0.56776003]],
                          [[ 2.36270298,  2.36904306],
                           [ 2.38090835,  2.38247847]]]])

# Compare your output to ours; difference should be around e-8
print('Testing conv_forward_naive')
print('difference: ', rel_error(out, correct_out))