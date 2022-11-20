import csv
import random
index = 0
typ_dyf = 0


header = ["index", "class"]

with open('score.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for i in range (0, 30000):
        typ_dyf = random.randint(0,4)
        data = [i, typ_dyf]
        writer.writerow(data)
    file.close()
