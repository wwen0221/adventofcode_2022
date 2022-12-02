with open('input.txt') as f:
    input = f.read()

calories = input.split('\n\n')
calories = [x.split('\n') for x in calories]
sum_list = []
for each_cal in calories:
    each_cal = [int(x) for x in each_cal]
    sum_list.append(sum(each_cal))
print(max(sum_list))

