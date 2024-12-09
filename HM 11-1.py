# импортируем с библиотеки Pillow модуль Image.
from PIL import ImageFilter, Image, ImageOps

# Открываем нашу картинку
image = Image.open('H2024.jpg')
# Применяем фильм размыстости(Blur)
blur_jp = image.filter(ImageFilter.BLUR)
# Сохраняем картинку.
blur_jp.save('blur_h20204.jpg')

image = Image.open('hp2025.jpg')
# Преобразование изображение в черное и белое.
grayscale_img = ImageOps.grayscale(image)
grayscale_img.save('grayscale.jpg')

image = Image.open('hps2025.jpg')
# Проверяем размер изображение
print(image.size)
new_size = (250, 250)
# Задаем новый размер
resized_img = image.resize(new_size)
resized_img.save('resized1.jpg')
# Проверяем размер картинки
print(resized_img.size)
