import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm_model(input_shape):
    model = Sequential([
        LSTM(256, return_sequences=True, input_shape=input_shape),
        LSTM(256),
        Dense(128, activation='relu'),
        Dense(88, activation='softmax')  # Output layer for 88 piano keys
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Example model
model = build_lstm_model((100, 3))  # 100 time steps, 3 features
model.summary()
