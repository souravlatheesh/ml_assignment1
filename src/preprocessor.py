from sklearn.preprocessing import StandardScaler

class Preprocessor:
    def _init_(self):
        self.scaler = StandardScaler()  # Initialize the StandardScaler

    def normalize(self, data, columns):
        data[columns] = self.scaler.fit_transform(data[columns])  # Use the initialized scaler
        return data

    def clean_data(self, data):
        data = data.dropna()  # Drop rows with missing values
        return data