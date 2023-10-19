import random
import matplotlib.pyplot as plt

def pie_chart(n):
    labels = []
    for i in range(1, n + 1):
        labels.append("Часть " + str(i))

    values = random.choices(range(1, 188), k=n)
    plt.figure(figsize=(17, 23))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Круговая диаграмма с " + str(n) + ' секторами')
    plt.show()

pie_chart(8)
