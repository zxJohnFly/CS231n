import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W.T)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train, num_dim = X.shape

  for i in xrange(num_train):
    scores = X[i,:].dot(W)
    scores -= np.max(scores)
    scores = np.exp(scores)
    loss += -np.log(scores[y[i]] / np.sum(scores))
    
    dW[y[i], :] -= X[i,:]
    dW += scores.reshape(W.shape[1],1).dot(X[i, :].reshape(1, num_dim))/np.sum(scores)

  loss /= num_train
  dW /= num_train

  loss += 0.5 * reg * np.sum(W * W)
  dW = dW.T
  dW += reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]

  scores = X.dot(W)
  scores_exp = np.exp(scores.T - np.max(scores, axis=1))
  loss = np.sum( -np.log(scores_exp[y,np.arange(num_train)]/np.sum(scores_exp, axis=0)))

  scores_exp = scores_exp / np.sum(scores_exp, axis=0)
  scores_exp[y,np.arange(num_train)] -= 1
  dW = scores_exp.dot(X)

  loss /= num_train
  dW /= num_train
  dW = dW.T

  loss += 0.5 * reg * np.sum(W * W)
  dW += reg * W


  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

