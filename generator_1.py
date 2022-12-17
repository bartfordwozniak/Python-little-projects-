import tensorflow as tf

# Pobranie frazy od użytkownika
phrase = input("Wprowadź frazę: ")

# Konwersja frazy na tensor ciągów znaków
phrase_tensor = tf.expand_dims(tf.expand_dims(tf.constant(phrase), 0), -1)

# Konwersja tensora ciągów znaków na tensor liczbowy
phrase_tensor = tf.strings.to_number(phrase_tensor, out_type=tf.int32)

# Normalizacja tensora do zakresu [0, 1]
normalized_phrase_tensor = (phrase_tensor - tf.reduce_min(phrase_tensor)) / (tf.reduce_max(phrase_tensor) - tf.reduce_min(phrase_tensor))

# Zmiana kształtu tensora na [32, 32]
image = tf.reshape(normalized_phrase_tensor, [32, 32])

# Wyświetlenie obrazka
import matplotlib.pyplot as plt
plt.imshow(image, cmap='gray')
plt.show()
