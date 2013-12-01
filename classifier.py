import math
import numpy as np

def runKMeans(k,patches,maxIter):
    """
    Runs K-means to learn k centroids, for maxIter iterations.

    Args:
      k - number of centroids.
      patches - 2D numpy array of size patchSize x numPatches
      maxIter - number of iterations to run K-means for

    Returns:
      centroids - 2D numpy array of size patchSize x k
    """
    # This line starts you out with randomly initialized centroids in a matrix
    # with patchSize rows and k columns. Each column is a centroid.
    centroids = np.random.randn(patches.shape[0],k)

    numPatches = patches.shape[1]

    for i in range(maxIter):
        # BEGIN_YOUR_CODE (around 19 lines of code expected)
        points = list()

        mapping = dict()
        for j in range(numPatches): #iterating over the patches
          point = patches[:,j]
          minindex = 0
          minvalue = float('inf')
          for l in range(k): #iterating over the centroids
            centroid = centroids[:,l]

            if l not in mapping:
              mapping[l] = set()
            distance = np.linalg.norm(centroid - point)
            if distance < minvalue:
              minindex = l
              minvalue = distance
          mapping[minindex].add(j)

        for centroid in mapping.keys():
          centroids[:,centroid] = np.mean(patches[np.ix_(range(patches.shape[0]),list(mapping[centroid]))], axis=1)
        # END_YOUR_CODE
    return centroids
