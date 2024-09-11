import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd
import os
from rps_bot import RPSBot

def load_or_create_model():
    model_path = 'models/rps_model.h5'
    if os.path.exists(model_path):
        print("Loading existing model...")
        model = Sequential([
            Dense(64, activation='relu', input_shape=(3,)),
            Dense(32, activation='relu'),
            Dense(3, activation='softmax')
        ])
        model.load_weights(model_path)
    else:
        print("Creating new model...")
        model = Sequential([
            Dense(64, activation='relu', input_shape=(3,)),
            Dense(32, activation='relu'),
            Dense(3, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

def prepare_data():
    data_path = 'data/game_history.csv'
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
    else:
        df = pd.DataFrame(columns=['player_move', 'bot_move', 'player_wins'])
    
    le = LabelEncoder()
    df['player_move'] = le.fit_transform(df['player_move'])
    df['bot_move'] = le.transform(df['bot_move'])
    
    X = df[['player_move', 'bot_move', 'player_wins']].values
    y = df['player_move'].shift(-1).fillna(0).astype(int).values
    
    return X, y

def train_model(model, X, y):
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, min_delta=0.001)
    model.fit(X[:-1], y[:-1], epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping])
    model.save_weights('models/rps_model.h5')

def main():
    bot = RPSBot()
    model = load_or_create_model()
    
    while True:
        print("\nRock-Paper-Scissors Bot")
        print("1. Play game")
        print("2. Train bot")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            play_game(bot, model)
        elif choice == "2":
            X, y = prepare_data()
            train_model(model, X, y)
            print("Bot trained successfully!")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def play_game(bot, model):
    while True:
        player_move = input("Enter your move (rock/paper/scissors): ").lower()
        if player_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Please try again.")
            continue
        
        bot_move = bot.predict_move(player_move, model)
        result = determine_winner(player_move, bot_move)
        
        print(f"\nPlayer move: {player_move}")
        print(f"Bot move: {bot_move}")
        print(result)
        
        save_game_result(player_move, bot_move, result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

def determine_winner(player_move, bot_move):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[player_move] == bot_move:
        return "Player wins!"
    elif beats[bot_move] == player_move:
        return "Bot wins!"
    else:
        return "It's a tie!"

def save_game_result(player_move, bot_move, result):
    df = pd.DataFrame({'player_move': [player_move], 'bot_move': [bot_move], 'player_wins': [result.startswith('Player')]})
    df.to_csv('data/game_history.csv', mode='a', index=False, header=not os.path.exists('data/game_history.csv'))

if __name__ == "__main__":
    main()