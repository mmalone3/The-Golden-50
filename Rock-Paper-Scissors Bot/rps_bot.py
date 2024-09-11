import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import random

class RPSBot:
    def __init__(self):
        self.le = LabelEncoder()
        self.le.fit(['rock', 'paper', 'scissors'])
    
    def predict_move(self, player_move, model):
        # Prepare input data
        X = np.array([[self.le.transform([player_move])[0], random.randint(0, 2), random.choice([0, 1])]])
        
        # Make prediction
        prediction = model.predict(X)[0]
        
        # Choose move based on prediction
        bot_move_index = np.argmax(prediction)
        bot_move = self.le.inverse_transform([bot_move_index])[0]
        
        return bot_move