import joblib
import os

class SvmModel:
    def __init__(self):
        self.model_dir = os.path.join(os.path.dirname(__file__), 'models')
        self.model_path = os.path.join(self.model_dir, 'svm_classifier.joblib')
        self.model = joblib.load(self.model_path)

    def predict(self, input_features):
        # Make predictions using the loaded SVM model
        prediction = self.model.predict(input_features)
        return prediction
