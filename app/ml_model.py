import numpy as np
import pickle
import os

class KidneyModel:
    def __init__(self):
        # We need to make sure we load the file from the correct path
        # The PKL file is at the root directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, 'Kidney.pkl')
        
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
        except Exception as e:
            print(f"Error loading model from {model_path}: {e}")
            self.model = None

    def predict(self, input_features):
        """
        Inputs: [sg, htn, hemo, dm, al, appet, rc, pc]
        Returns: Prediction value (1 or 0)
        """
        if not self.model:
            raise ValueError("Model is not loaded.")
            
        values = np.array([input_features])
        prediction = self.model.predict(values)
        return prediction[0]

# Singleton instance for routes to import
kidney_model = KidneyModel()
