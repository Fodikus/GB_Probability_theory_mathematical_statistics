import matplotlib.pyplot as plt
from math import factorial

def combinatorics(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

### Создание области отрисовки
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_axis_off()

formula = 'Задача 1. \n'
formula = formula + 'Из колоды в 52 карты извлекаются случайным образом 4 карты. \n'
formula = formula + 'б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз. \n'
formula = formula + 'Необходиом использовать формулу сочетания комбинаторики \n'
formula = formula + '$\\ C^k_n = \\frac{n!}{k!\\left(n-k\\right)!}  $\n'
formula = formula + 'и классическую формулу вероятности. \n'
formula = formula + '$\\ P(A) = \\frac{m}{n} $\n'
formula = formula + 'и классическую формулу вероятности. \n'
formula = formula + '$\\ P(A) = \\frac{m}{n} $\n'
formula = formula + 'Так же использовать то, что сумма вероятности противоположных событий равно 1 \n'
formula = formula + '$\\ P(A) + P( \\overline{A})=\\ {1} $\n'
formula = formula + 'где '
formula = formula + '$\\ P( \\overline{A}) $'
formula = formula + ' - исход, когда из 4-х извлеченных карт не оказалось ни одного туза. \n'
formula = formula + 'm количество способов извлечь 4 карты из колоды без тузов, соответственно 52-4=48 \n'
formula = formula + '$\\ m : \\ C^k_n = С^{4}_{48} $ \n'
formula = formula + 'а n количество способов извлечь 4 карты из 52 карт. \n'
formula = formula + '$\\ n : \\ C^k_n = С^{4}_{52} $\n'
formula = formula + 'тогда \n'
formula = formula + '$\\ P(A) = {1} - P( \\overline{A}) $\n'
formula = formula + '\n'

# Вычислим  m
m = combinatorics(48, 4)
formula = formula + 'Вычислим  m:\n'
formula = formula + 'm=' + str(m) + '\n'

# Вычислим  n
n = combinatorics(52, 4)
formula = formula + 'Вычислим  n:\n'
formula = formula + 'n=' + str(n) + '\n'

# Вычислим  P
P = 1 - m / n
formula = formula + 'Вычислим  P:\n'
formula = formula + 'P=' + str(round(P,4)) + '\n'

# Ответ
result = P * 100
formula = formula + 'Вероятность того, что хотя бы 1 карта туз:\n'
formula = formula + 'P=' + str(round(result,2)) + '%'

### Отрисовка формулы
t = ax.text(0.5, 0.5, formula,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=20, color='black')
  
### Определение размеров формулы
ax.figure.canvas.draw()
bbox = t.get_window_extent()
bbox.width, bbox.height

# Установка размеров области отрисовки dpi=80
fig.set_size_inches(bbox.width/80,bbox.height/80)

### Отрисовка или сохранение формулы в файл
plt.show()


