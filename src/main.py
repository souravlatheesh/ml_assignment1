# main.py
from data_handler import DataHandler
from preprocessor import Preprocessor
from model_trainer import ModelTrainer
from recommendation_engine import NutritionRecommender

if __name__ == "__main__":
    # Initialize file paths and features
    data_file = "/Users/sour_v/Documents/ML ops/nutri_recommender/data/food_data.csv"
    output_file = "cleaned_data.csv"
    feature_columns = ['Calories', 'Protein', 'Fat', 'Carbs']
    
    # Load and preprocess data
    data_handler = DataHandler(filepath=data_file)
    data = data_handler.load_data()

    preprocessor = Preprocessor()
    data = preprocessor.clean_data(data)
    data = preprocessor.normalize(data, feature_columns)
    
    # Train model
    trainer = ModelTrainer()
    model = trainer.train(data, feature_columns)
    
    # Create recommender engine
    recommender = NutritionRecommender(model, data)
    
    # Example user preferences input (Calories, Protein, Fat, Carbs)
    user_preferences = [120, 3, 1.5, 22]
    
    # Get recommendations
    recommendations = recommender.recommend(user_preferences)
    print("Recommended foods based on your preferences:")
    print(recommendations)