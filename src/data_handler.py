import pandas as pd

class DataHandler:
    def _init_(self, filepath):
        self.filepath = '/Users/sour_v/Documents/ML ops/nutri_recommender/data/food_data.csv'  
    def load_data(self):
        try:
            data = pd.read_csv(self.filepath)
            return data
        except FileNotFoundError:
            print("File not found!")
            return None

    def save_data(self, data, output_path):
        data.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")