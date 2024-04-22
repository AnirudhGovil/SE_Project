import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.cluster import MeanShift

class CourseModel:
    """
    Abstract class for course recommendation models.
    """
    def fit(self, X):
        """
        Fits the model to the data.

        Parameters:
        - X: The training data.

        Returns:
        - None
        """
        pass

    def recommend(self, user_preferences):
        """
        Recommends courses based on the user's preferences.

        Parameters:
        - user_preferences: The user's preferences for each feature.

        Returns:
        - indices: The indices of the recommended courses.
        """
        pass

class KNNModel(CourseModel):
    """
    A class to represent a k-nearest neighbors model for course recommendation.
    """
    def __init__(self, n_neighbors=3):
        """
        Initializes the model.

        Parameters:
        - n_neighbors: The number of neighbors to consider.
        """
        self.n_neighbors = n_neighbors
        self.knn = None

    def fit(self, X):
        """
        Fits the model to the data.

        Parameters:
        - X: The training data.
        """
        self.knn = NearestNeighbors(n_neighbors=self.n_neighbors)
        self.knn.fit(X)

    def recommend(self, user_preferences):
        """
        Recommends courses based on the user's preferences.

        Parameters:
        - user_preferences: The user's preferences for each feature.

        Returns:
        - indices: The indices of the recommended courses.
        """
        _, indices = self.knn.kneighbors(user_preferences.reshape(1, -1))
        return indices[0]
    
class RadiusNeighborsModel(CourseModel):
    """
    A class to represent a radius neighbors model for course recommendation.
    """
    def __init__(self, radius=1.0):
        """
        Initializes the model.

        Parameters:
        - radius: The radius within which to consider neighbors.
        """
        self.radius = radius
        self.rnc = None

    def fit(self, X, y):
        """
        Fits the model to the data.

        Parameters:
        - X: The training data.
        - y: The target labels.
        """
        self.rnc = RadiusNeighborsClassifier(radius=self.radius)
        self.rnc.fit(X, y)

    def recommend(self, user_preferences):
        """
        Recommends courses based on the user's preferences.

        Parameters:
        - user_preferences: The user's preferences for each feature.

        Returns:
        - indices: The indices of the recommended courses.
        """
        indices = self.rnc.radius_neighbors(user_preferences.reshape(1, -1))
        return indices[0]
    
class MeanShiftModel(CourseModel):
    """
    A class to represent a mean shift model for course recommendation.
    """
    def __init__(self, bandwidth=2):
        """
        Initializes the model.

        Parameters:
        - bandwidth: The bandwidth of the kernel.
        """
        self.bandwidth = bandwidth
        self.ms = None

    def fit(self, X):
        """
        Fits the model to the data.

        Parameters:
        - X: The training data.
        """
        self.ms = MeanShift(bandwidth=self.bandwidth)
        self.ms.fit(X)

    def recommend(self, user_preferences):
        """
        Recommends courses based on the user's preferences.

        Parameters:
        - user_preferences: The user's preferences for each feature.

        Returns:
        - indices: The indices of the recommended courses.
        """
        labels = self.ms.predict(user_preferences.reshape(1, -1))
        indices = np.where(self.ms.labels_ == labels[0])[0]
        return indices
