import joblib
import random

class MLAgent:
    def __init__(self, model_path='models/model.pkl'):
        try:
            self.model = joblib.load(model_path)
        except:
            self.model = None

    def predict_next_move(self, last_moves):
        if not self.model or len(last_moves) < 3:
            return random.choice(['Rock', 'Paper', 'Scissors'])

        X = [[self._move_to_int(m) for m in last_moves[-3:]]]
        predicted = self.model.predict(X)[0]
        return self._counter_move(predicted)

    def _move_to_int(self, move):
        return {'Rock': 0, 'Paper': 1, 'Scissors': 2}[move]

    def _counter_move(self, move):
        return {
            0: 'Paper',     # Rock -> Paper
            1: 'Scissors',  # Paper -> Scissors
            2: 'Rock'       # Scissors -> Rock
        }[move]
