from matplotlib import pyplot as plt

plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "Статистически значимая величина", fontsize=15, weight='bold')
plt.text(0.57, 0.9, "- это величина (или более", fontsize=15)
plt.text(0.01, 0.8, "крайние величины) появление кторой случайным образом", fontsize=15)
plt.text(0.01, 0.7, "маловероятно.", fontsize=15)
plt.text(0.01, 0.6, "Нулевая гипотеза", fontsize=15, weight='bold')
plt.text(0.3, 0.6, "- это предположение, принимаемое по", fontsize=15)
plt.text(0.01, 0.5, "молчанию о том, что два наблюдаемых события не имеют связи.", fontsize=15)
plt.text(0.01, 0.4, "Алтернативная гипотеза", fontsize=15, weight='bold')
plt.text(0.4, 0.4, "- утверждает, что связь наборот есть.", fontsize=15)
plt.text(0.01, 0.3, "P – value", fontsize=15, weight='bold')
plt.text(0.15, 0.3, "- если нулевая гипотеза верна, то это вероятность", fontsize=15)
plt.text(0.01, 0.2, "получить значение статистики такое же или более экстремальное,", fontsize=15)
plt.text(0.01, 0.1, "по сравнению с ранее наблюдаемым для данной вероятностной", fontsize=15)
plt.text(0.01, 0.01, "модели распределения значений случайной величины.", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show()