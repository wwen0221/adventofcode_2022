
def main():
    sum_list = []
    cycles_to_check = [20,60,100,140,180,220]

    with open('input.txt') as f:
        input = f.readlines()
        current_cycle = 0
        x = 1


        for instruction in input:
            print(instruction)
            if 'noop' in instruction:
                current_cycle += 1
                if current_cycle in cycles_to_check:
                    sum_list.append(current_cycle*x)

            else:
                number_to_add = int(instruction.split(' ')[-1])
                times = 0
                while times <2:
                    current_cycle+=1
                    if current_cycle in cycles_to_check:
                        sum_list.append(current_cycle * x)

                    times+=1
                x+=number_to_add

    print(sum(sum_list))

if __name__ == '__main__':
    main()