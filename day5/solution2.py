import re


def main():

    with open('input.txt') as f:
        input = f.read()

    stacks, instructions = input.split('\n\n')
    last_line = stacks.split('\n')[-1]

    extracted_list = []

    for idx, number in enumerate(last_line):
        current_list = []
        if number != ' ':
            for row in stacks.split('\n')[:-1]:
                if len(row)>idx:
                    if row[idx] != ' ':
                            current_list.insert(0,row[idx])

        if len(current_list) > 0:
            extracted_list.append(current_list)
    print(extracted_list)

    for instruction in instructions.split('\n'):
        print(instruction)
        no_to_move = int(re.search('move(.*)from', instruction).group(1))
        move_from =  int(re.search('from(.*)to', instruction).group(1))-1
        move_to =  int(re.search('to(.*)', instruction).group(1))-1

        if no_to_move == 1:
            for crate_to_pop in range(no_to_move):
                popped_crate = extracted_list[move_from].pop()
                extracted_list[move_to].append(popped_crate)
        else:
            popped_crate = extracted_list[move_from][-no_to_move:]
            print(popped_crate)
            if no_to_move == len(extracted_list[move_from]):
                extracted_list[move_from] = []
            else:
                extracted_list[move_from] = extracted_list[move_from][
                                            :-no_to_move]

            extracted_list[move_to] = extracted_list[move_to]+popped_crate

        print(extracted_list)

    l = [item[-1] for item in extracted_list]
    print(''.join(l))




if __name__ == '__main__':
    main()