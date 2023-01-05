# zaimportuj potrzebne biblioteki
import tensorflow as tf
import numpy as np

# pobierz dane treningowe (zestaw zdjęć owoców)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fruits_360.load_data() # tf.keras.datasets.fruits_360 nie jest
                                                                                # dostępna w wersji TensorFlow, której używasz.
                                                                                # Możliwe, że biblioteka ta została usunięta lub zmieniona
                                                                                # w nowszej wersji TensorFlow.

# przygotuj dane treningowe (normalizuj i zmień na float32)
x_train = x_train / 255.0
x_test = x_test / 255.0
x_train = x_train.astype(np.float32)
x_test = x_test.astype(np.float32)

# zbuduj model z wykorzystaniem konwolucyjnej sieci neuronowej
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(100, 100, 3)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3,3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(len(np.unique(y_train)), activation='softmax'))

# skompiluj model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# wytrenuj model
model.fit(x_train, y_train, epochs=10)

# ocen model na danych testowych
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
