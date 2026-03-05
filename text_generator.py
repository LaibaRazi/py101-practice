import os
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation, Input
from tensorflow.keras.optimizers import RMSprop

# -------------------------------
# 1️⃣ Download dataset
# -------------------------------
filepath = tf.keras.utils.get_file(
    'shakespeare.txt',
    'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'
)

text = open(filepath, 'rb').read().decode(encoding='utf-8').upper()
text = text[300000:400000]  # smaller slice to prevent memory crash

# -------------------------------
# 2️⃣ Prepare character mapping
# -------------------------------
characters = sorted(set(text))
char_to_index = {c: i for i, c in enumerate(characters)}
index_to_char = {i: c for i, c in enumerate(characters)}

# -------------------------------
# 3️⃣ Create sequences
# -------------------------------
seq_length = 40
step_size = 3

sentences = []
next_chars = []

for i in range(0, len(text) - seq_length, step_size):
    sentences.append(text[i:i + seq_length])
    next_chars.append(text[i + seq_length])

# -------------------------------
# 4️⃣ One-hot encode
# -------------------------------
x = np.zeros((len(sentences), seq_length, len(characters)), dtype=np.float32)
y = np.zeros((len(sentences), len(characters)), dtype=np.float32)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_index[char]] = 1
    y[i, char_to_index[next_chars[i]]] = 1

# -------------------------------
# 5️⃣ Build model
# -------------------------------
model = Sequential()
model.add(Input(shape=(seq_length, len(characters))))  # fix input warning
model.add(LSTM(128))
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))

# -------------------------------
# 6️⃣ Train model
# -------------------------------
model.fit(x, y, batch_size=256, epochs=5)

# -------------------------------
# 7️⃣ Save model correctly
# -------------------------------
# model.save('text_generator.keras')
# print("Model saved successfully!")

# -------------------------------
# 8️⃣ Load model (optional)
# -------------------------------
# model = tf.keras.models.load_model('text_generator.keras')
# print("Model loaded successfully!")

# -------------------------------
# 9️⃣ Text generation function
# -------------------------------
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-8) / temperature  # avoid log(0)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_text(length=400, temperature=0.5):
    start_index = random.randint(0, len(text) - seq_length - 1)
    generated = ''
    sentence = text[start_index:start_index + seq_length]
    generated += sentence

    for i in range(length):
        x_pred = np.zeros((1, seq_length, len(characters)), dtype=np.float32)
        for t, char in enumerate(sentence):
            x_pred[0, t, char_to_index[char]] = 1

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_char = index_to_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

    return generated

# Example usage:
print("Generated Text:\n")
print(generate_text(length=300, temperature=0.5),"\n")