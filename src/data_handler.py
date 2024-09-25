import pandas as pd

class DataHandler:
    def __init__(self, filepath):  # Accepts filepath as an argument
        self.filepath = filepath
    
    def load_data(self):
        try:
            data = pd.read_csv(self.filepath)  # Uses the filepath passed in the constructor
            return data
        except FileNotFoundError:
            print(f"File not found at {self.filepath}!")
            return None

    def save_data(self, data, output_path):
        data.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")