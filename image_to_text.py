import base64
import sys

# Otwieramy plik graficzny i odczytujemy zawartość jako bajty
with open(sys.argv[1], 'rb') as image_file:
    image_content = image_file.read()

# Kodujemy bajty jako tekst w formacie base64
encoded_image = base64.b64encode(image_content).decode('utf-8')

# Otwieramy plik tekstowy i zapisujemy zakodowaną grafikę
with open(sys.argv[2], 'w') as text_file:
    text_file.write(encoded_image)
