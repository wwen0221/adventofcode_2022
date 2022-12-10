
def main():
    sprite_pos = [0,1,2]
    current_pixel = 0
    current_row = 0
    final_d = {}

    with open('input.txt') as f:
        input = f.readlines()
        temp_list = []

        for instruction in input:
            if 'noop' in instruction:
                if current_pixel in sprite_pos:
                    temp_list.append('#')
                else:
                    temp_list.append('.')
                current_pixel += 1

                if current_pixel ==40:
                    final_d[current_row] = temp_list
                    temp_list = []
                    current_row+=1
                    current_pixel = 0


            else:
                number_to_add = int(instruction.split(' ')[-1])
                times = 0
                while times < 2:
                    if current_pixel in sprite_pos:
                        temp_list.append('#')
                    else:
                        temp_list.append('.')
                    current_pixel += 1

                    if current_pixel ==40:
                        final_d[current_row] = temp_list
                        temp_list = []
                        current_row += 1
                        current_pixel = 0

                    times += 1

                sprite_pos = [x + number_to_add for x in sprite_pos]


    for row, val in final_d.items():
        print(''.join(val))

if __name__ == '__main__':
    main()