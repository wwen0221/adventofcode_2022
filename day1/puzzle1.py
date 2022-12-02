with open('input.txt') as f:
    input = f.read()

calories = input.split('\n\n')
calories = [x.split('\n') for x in calories]
sum_list = []
for each_cal in calories:
    each_cal = [int(x) for x in each_cal]
    sum_list.append(sum(each_cal))

sorted_sum_list = sum_list.sort(reverse=True)

print(f'Max calories an elf is carrying: {max(sum_list)}')
print(f'Top 3 calories: {sum_list[:3]}')
print(f'Sum of Top 3: {sum(sum_list[:3])}')
