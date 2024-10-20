from PIL import Image, ImageFilter, ImageDraw, ImageFont

# Библиотека PIL  ответвление библиотеки pillow, работает с изображениями
# указываем путь к файлам, открываем их, загружаем и .show показывает изображение
name = "original-pictures/koshka.jpg"
with Image.open(name) as img:
    img.load()
    #img.show()
# Необходимо понимать значение и научится работать с тремя ключевыми свойствами объектов, порождаемых классом Image.
# Доступ ко всем этим трем свойствам вышеназванного класса можно получить через его соответствующие одноименные
# атрибуты, как .format, .size и .mode:
print(img.format, img.size, img.mode)        # покажет JPEG (1920, 1273) RGB
rotated = img.rotate(180)     # метод позволяет повернуть изобразение на любое количество градусов, указываем в скобках
img = img.resize((800, 600))    # меняем разрешение, которое указываем кортежом 800, 600
img.save(name)
font = ImageFont.truetype("arial.ttf", size=20)
idraw = ImageDraw.Draw(img)
idraw.text((25, 25), 'ЭТО КОШКА', font=font)
img.save(name)
img = Image.open(name)
img.show()

# пользуясь классами ImageDraw, ImageFont добавляем текст на картинки


