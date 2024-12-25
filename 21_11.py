# 1. Создаем список, который содержит два внутренних списка
outer_list = [[], []]

# 2. Добавляем число в один из внутренних списков
outer_list[0].append(5)  
outer_list[0].append(10) 

# 3. Удаляем первое число из одного из внутренних списков
if outer_list[0]:  
    outer_list[0].pop(0)  

# 4. Считаем сумму чисел в каждом внутреннем списке и добавляем ее в конец списка
for inner_list in outer_list:
    total_sum = sum(inner_list)  
    inner_list.append(total_sum)  
# 5. Выводим весь список
print(outer_list)
