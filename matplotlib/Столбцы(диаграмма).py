import random
import matplotlib.pyplot as plt

def bar_chartd():
    l = [str(i) for i in range(1, 8)] 
    v= random.choices(range(1, 101), k=7) 
    plt.bar(l, v)
    plt.title("Столбчатая диаграмма с рандомными значениями")
    plt.xlabel("Столбцы")
    plt.ylabel("Значения")
    plt.show()

bar_chartd()
