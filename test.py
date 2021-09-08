# object_list = ["Документация", "Сборочные единицы", "Детали", "Стандартные изделия", "Болты"]
# spc_list = ["Документация", "", "", "Сборочные единицы", "сборка", "Детали", "", "Стандартные изделия", "абырабыр", "Болты"]
# obj_to_del = []
# # a=[""]
# indexes = []

# for i in range(len(object_list)):
#     if object_list[i] in spc_list:
#         indexes.append(spc_list.index(object_list[i]))
# print(indexes)

# for i in range(len(indexes)-1):
#     if indexes[i+1] - indexes[i] > 1:
#         obj_to_del = spc_list[indexes[i]:indexes[i+1]]
#         if obj_to_del[1:] == [""]*(len(obj_to_del)-1):
#             print(obj_to_del)

# a = [1, 3, 7, 12, 5, 8, 9]
# for i in range(len(a)):
# 	if a[i] != a[len(a)-1]:
# 		print(a[i], a[i+1])



# # 	def del_spc_spw_objects(objects_in_spc, iSpecification, iDocumentSpc):
#             objects_to_del = []
#             indexes = []
#             indexes_list = []
#             object_list = ["Сборочные единицы", "Детали", "Стандартные изделия", "Болты",
#                             "Винты", "Втулки"]
#             spc_spw_list = []
#             dictionary = {}

#             for obj in enumerate(objects_in_spc):
#                 sp_col = iSpecification.ksGetSpcObjectColumnText(obj[1], 6,  1, 0)
#                 sp_naim = iSpecification.ksGetSpcObjectColumnText(obj[1], 5,  1, 0)
#                 if sp_naim in object_list:
#                     indexes.append(obj[0])

#                 spc_spw_list.append([obj[0], obj[1], sp_naim, sp_col])

#             spc_list = [x for x in spc_spw_list if x[3] not in ("1111", "2222")]

#             for i in range(len(indexes)):
#                 if indexes[i] != indexes[len(indexes)-1]:
#                     indexes_list.append((indexes[i], indexes[i+1]))
#             print(indexes_list)

#             for i in range(len(indexes_list)):
#                 for j in range(indexes_list[i][0], indexes_list[i][1]+1):
#                     print(j)
#                     if spc_list[j][0] == j:
#                         print(spc_list[j])

#                 print("--------")

def func():
	return 23, 13

a = func()
print(a[1])