from sklearn.neighbors import NearestNeighbors

class CourseModel:
    def fit(self, X):
        pass

    def recommend(self, user_preferences):
        pass

class KNNModel(CourseModel):
    def __init__(self, n_neighbors=3):
        self.n_neighbors = n_neighbors
        self.knn = None

    def fit(self, X):
        self.knn = NearestNeighbors(n_neighbors=self.n_neighbors)
        self.knn.fit(X)

    def recommend(self, user_preferences):
        _, indices = self.knn.kneighbors(user_preferences.reshape(1, -1))
        return indices[0]