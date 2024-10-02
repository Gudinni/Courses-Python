#Задача №1

nums = [1,2,7,11,15,9,6]
target = 16

def find_sum_elements(nums, target):
    my_dict = {}
    for key, value in enumerate(nums):
        sum = target - value
        if sum in my_dict:
            return [my_dict[sum], key]
        my_dict[value] = key





#Задача #2
s = 'Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства'


def is_pangram(s):
    russian_alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    s = s.replace(' ', '').lower()
    for i in russian_alphabet:
        if i not in s:
            return False
            
    return True
   


print(f'Индексы числа {target} равны {find_sum_elements(nums, target)}')
print(is_pangram(s))
