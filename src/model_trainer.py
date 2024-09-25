# model_trainer.py
from sklearn.neighbors import NearestNeighbors

class ModelTrainer:
    def __init__(self, n_neighbors=5):
        self.model = NearestNeighbors(n_neighbors=n_neighbors)
    
    def train(self, data, features):
        X = data[features]
        self.model.fit(X)
        return self.model