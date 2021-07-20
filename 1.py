# 0 - Обозначение, 1 - Наименование, 2 - Кол на сборке, 3 - Количество на изд, 4 - Масса
base_spc_element = ["Сборочные единицы", "Детали", "Стандартные изделия", "Прочие изделия", "Материалы"]
between_base_object = False
# print("Изначальный флаг: ", between_base_object)
# first_iter = True
# list_of_mass = []
new_list = []

my_list = [["", "Сборочные единицы", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "Детали", "", "", ""], ["", "ыва", "2", "2", "0,005"], ["", "", "", "", ""], ["", "Материалы", "", "", ""]]

list_of_elements = []
i = 0
for element in my_list:
	if element[1] in base_spc_element:
		list_of_elements.append(i)
		i += 1
	else: 
		i += 1
print(list_of_elements)

while len(list_of_elements) > 1:
	for i in range(list_of_elements[0] + 1, list_of_elements[1]):
		if my_list[i][4] != "":
			new_list.append(f"Масса есть в элементе {i}")
	if new_list == []:
		del list_of_elements[0]
print(new_list)








# 
# for i in range(0, len(my_list)):
# 	if first_iter:
# 		if my_list[i][1] in base_spc_element:
# 			between_base_object = not between_base_object
# 			print(between_base_object)
# 			first_iter = False
			
# 	else:
# 		if my_list[i][1] in base_spc_element:
# 			between_base_object = not between_base_object
# 			print(between_base_object)
# 			if list_of_mass == []:
# 				print(f"Удаляем предыдущие элементы")
# 				between_base_object = not between_base_object
# 				print(between_base_object)

# 	if my_list[i][4] != "" and between_base_object == True:
# 		list_of_mass.append("Здесь есть масса")

# 	print(list_of_mass)
	
	
		
		
