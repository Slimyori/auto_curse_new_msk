# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

# new_slovo = []
# new_slovo.append(random.choice(randomikulus))
import random

# Генератор name_gen создает строку из двух переменных, слово один и слово два, с помощью форматированной строки добавляем пробел для условия
def name_gen():
	randomikulus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
					"u", "v", "w", "x", "y", "z"]
	new_slovo_one = ""
	new_slovo_dva = ""
	while True: #У нас в вебинаре не было показано как сделать бесконечный генератор, подсмотрел на скилбокс как сделать конкретно бесконечную последовательность https://skillbox.ru/media/code/generatory_python_chto_eto_takoe_i_zachem_oni_nuzhny/
		for i in range(random.randrange(1, 16)): #C помощью in range создаем случайную длинну слова
			new_slovo_one += random.choice(randomikulus)# Наполняем слово буквами

		for i in range(random.randrange(1, 16)):# Повторяем для второго слова
			new_slovo_dva += random.choice(randomikulus)

		yield f"{new_slovo_one} {new_slovo_dva}"# Возвращаем строку с именем слепленным из слова один и слова два
		new_slovo_one = ""
		new_slovo_dva = ""# Обнуляем строки что бы они не перенаполнялись


kvant = name_gen() #наделяем переменную строкой которую возвращает yield в генераторе name_gen
print(next(kvant))
print(next(kvant))
print(next(kvant))
print(next(kvant)) #Пример работы программы

