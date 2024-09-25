from sklearn.preprocessing import StandardScaler

class Preprocessor:
    def _init_(self):
        self.scaler = StandardScaler()

    def normalize(self, data, columns):
        data[columns] = self.scaler.fit_transform(data[columns])
        return data
    
    def clean_data(self, data):
        data = data.dropna()
        return data