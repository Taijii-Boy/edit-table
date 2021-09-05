object_list = ["Документация", "Сборочные единицы", "Детали", "Стандартные изделия", "Болты"]
spc_list = ["Документация", "", "", "Сборочные единицы", "сборка", "Детали", "", "Стандартные изделия", "абырабыр", "Болты"]
obj_to_del = []


a=[""]
indexes = []
for i in range(len(object_list)):
    if object_list[i] in spc_list:
        indexes.append(spc_list.index(object_list[i]))

for i in range(len(indexes)-1):
    if indexes[i+1] - indexes[i] > 1:
        obj_to_del = spc_list[indexes[i]:indexes[i+1]]
        if obj_to_del[1:] == a*(len(obj_to_del)-1):
            print(obj_to_del)