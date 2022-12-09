visited_position= {}

def update_tail(H,T):
    row_diff, col_diff = abs(H[0] - T[0]), abs(H[1]- T[1])

    if row_diff>1 and col_diff==0:
        #update row only
        if H[0] > T[0]:
            T[0] += 1
        else:
            T[0] -= 1

    if row_diff==0 and col_diff>1:
        print('update col')
        #update col only
        if H[1] > T[1]:
            T[1] += 1
        else:
            T[1]-=1

    if row_diff>0 and col_diff>1 or row_diff>1 and col_diff>0:
        #update both
        if H[1] > T[1]:
            T[1] += 1
        else:
            T[1] -= 1

        if H[0] > T[0]:
            T[0] += 1
        else:
            T[0] -=1


    # add visited position to dictionary
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

    visited_position[','.join(map(str, T))] = 1

    with open('input.txt') as f:
        input = f.readlines()
        for instruction in input:
            direction, times = instruction.split(' ')

            for time in range(int(times)):
                if direction=='R':
                    H[1]+=1
                    H, T = update_tail(H, T)

                if direction == 'L':
                    H[1] -= 1
                    H, T = update_tail(H, T)

                if direction == 'U':
                    H[0] += 1
                    H, T = update_tail(H, T)

                if direction == 'D':
                    H[0] -= 1
                    H,T = update_tail(H,T)


        print(len(visited_position))

if __name__ == '__main__':
    main()