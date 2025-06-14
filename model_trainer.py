import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

def train_model(data_path='data/game_data.csv', model_path='models/model.pkl'):
    df = pd.read_csv(data_path)

    if len(df) < 50:
        print("Yeterli veri yok.")
        return

    # Verileri kontrol et
    print(f"Toplam veri satırı: {len(df)}")
    print("İlk 5 satır:")
    print(df.head())

    X = df[['move_1', 'move_2', 'move_3']]
    y = df['next_move']

    try:
        model = LogisticRegression(max_iter=200)
        model.fit(X, y)
    except Exception as e:
        print("Model eğitimi sırasında hata:", e)
        return

    try:
        os.makedirs('models', exist_ok=True)
        joblib.dump(model, model_path)
        print("Model başarıyla eğitildi ve kaydedildi.")
    except Exception as e:
        print("Model dosyası kaydedilirken hata oluştu:", e)

if __name__ == '__main__':
    train_model()
