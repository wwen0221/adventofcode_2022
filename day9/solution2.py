visited_position= {}

def update_tail(H,T,number):
    print(H)
    print(T)
    row_diff, col_diff = abs(H[0] - T[0]), abs(H[1]- T[1])
    print('row_diff', row_diff)
    print('col_diff', col_diff)

    if row_diff>1 and col_diff==0:
        print('update row')
        #update row only
        if H[0] > T[0]: #head on the right side
            T[0] += 1 #add visited position to dictionary
        else:
            T[0] -= 1

    if row_diff==0 and col_diff>1:
        print('update col')
        #update col only
        if H[1] > T[1]: #head on the up side
            T[1] += 1 #add visited position to dictionary
        else:
            T[1]-=1

    if row_diff>0 and col_diff>1 or row_diff>1 and col_diff>0:
        print('update both')
        #update both
        if H[1] > T[1]:
            T[1] += 1
        else:
            T[1] -= 1

        if H[0] > T[0]:
            T[0] += 1
        else:
            T[0] -=1

    if number == 'nine':
        # add visited position to dictionary
        print(f'updated to {T}')
        position = ",".join(str(item) for item in T)
        if position not in visited_position.keys():
            visited_position[position]=1
        else:
            visited_position[position]+=1

        print(visited_position)

    return H,T

def main():

    H = [1000,1000]
    one = [1000,1000]
    two= [1000,1000]
    three= [1000,1000]
    four= [1000,1000]
    five= [1000,1000]
    six= [1000,1000]
    seven= [1000,1000]
    eight= [1000,1000]
    nine= [1000,1000]

    visited_position[','.join(map(str, H))] = 1

    with open('input.txt') as f:
        input = f.readlines()
        for instruction in input:
            direction, times = instruction.split(' ')
            print(f'direction {direction}')
            print(f'times {times}')

            for time in range(int(times)):
                if direction=='R':
                    H[1]+=1
                    H, one = update_tail(H, one,'one')
                    one, two = update_tail(one, two, 'two')
                    two, three = update_tail(two, three, 'three')
                    three, four = update_tail(three, four, 'four')
                    four, five = update_tail(four, five, 'five')
                    five, six = update_tail(five, six, 'six')
                    six, seven = update_tail(six, seven, 'seven')
                    seven, eight = update_tail(seven, eight, 'eight')
                    eight, nine = update_tail(eight, nine, 'nine')

                if direction == 'L':
                    H[1] -= 1
                    H, one = update_tail(H, one,'one')
                    one, two = update_tail(one, two, 'two')
                    two, three = update_tail(two, three, 'three')
                    three, four = update_tail(three, four, 'four')
                    four, five = update_tail(four, five, 'five')
                    five, six = update_tail(five, six, 'six')
                    six, seven = update_tail(six, seven, 'seven')
                    seven, eight = update_tail(seven, eight, 'eight')
                    eight, nine = update_tail(eight, nine, 'nine')

                if direction == 'U':
                    H[0] += 1
                    H, one = update_tail(H, one,'one')
                    one, two = update_tail(one, two, 'two')
                    two, three = update_tail(two, three, 'three')
                    three, four = update_tail(three, four, 'four')
                    four, five = update_tail(four, five, 'five')
                    five, six = update_tail(five, six, 'six')
                    six, seven = update_tail(six, seven, 'seven')
                    seven, eight = update_tail(seven, eight, 'eight')
                    eight, nine = update_tail(eight, nine, 'nine')

                if direction == 'D':
                    H[0] -= 1
                    H, one = update_tail(H, one,'one')
                    one, two = update_tail(one, two, 'two')
                    two, three = update_tail(two, three, 'three')
                    three, four = update_tail(three, four, 'four')
                    four, five = update_tail(four, five, 'five')
                    five, six = update_tail(five, six, 'six')
                    six, seven = update_tail(six, seven, 'seven')
                    seven, eight = update_tail(seven, eight, 'eight')
                    eight, nine = update_tail(eight, nine, 'nine')


        print(len(visited_position))

if __name__ == '__main__':
    main()