import matplotlib.pyplot as plt

# Математические уравнения с пояснением
equations = r"""
$1. x(u) = 3e^u - u^2 - 2u - 2, \quad x(0) = 1 $ 
$ x'(u) = 3e^u - 2u - 2, \quad x'(0) = 1 $ 
$ x''(u) = 3e^u - 2, \quad x''(0) = 1 $ 
$ x'''(u) = 3e^u, \quad x'''(0) = 3 $ 
$ x''''(u) = 3e^u, \quad x''''(0) = 3 $ 
$ x(u) = 1 + u + \frac{u^2}{2} + \frac{u^3}{2} + \frac{u^4}{8} + \dots $
"""

# Создание фигуры и настройка
fig, ax = plt.subplots(figsize=(8, 6))  # Увеличенный размер изображения для большего пространства
ax.text(
    0.5, 0.5,  # Положение текста (по центру)
    equations, 
    fontsize=18,  # Увеличенный шрифт для улучшения читаемости
    ha='center', va='center',  # Выравнивание текста
    linespacing=2  # Увеличение расстояния между строками
)
ax.axis('off')  # Убираем оси для чистого вида

# Сохранение и отображение изображения
plt.savefig("taylor.png", dpi=300, bbox_inches='tight')  # Высокое качество изображения
plt.show()
