class NutritionRecommender:
    def _init_(self, model, data):
        self.model = model
        self.data = data

    def recommend(self, user_preferences, n_recommendations=5):
        distances, indices = self.model.kneighbors([user_preferences], n_neighbors=n_recommendations)
        recommendations = self.data.iloc[indices[0]]
        return recommendations[['Food Item', 'Calories', 'Protein', 'Fat', 'Carbs']]