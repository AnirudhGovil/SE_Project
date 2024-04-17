from sklearn.neighbors import NearestNeighbors

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