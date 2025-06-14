import pandas as pd
import os

def save_game_data(moves, next_move, data_path='data/game_data.csv'):
    os.makedirs('data', exist_ok=True)
    
    row = {
        'move_1': moves[0],
        'move_2': moves[1],
        'move_3': moves[2],
        'next_move': next_move
    }

    df = pd.DataFrame([row])

    # Eğer dosya yoksa başlık satırı yaz
    if not os.path.exists(data_path):
        df.to_csv(data_path, mode='w', header=True, index=False)
    else:
        df.to_csv(data_path, mode='a', header=False, index=False)
