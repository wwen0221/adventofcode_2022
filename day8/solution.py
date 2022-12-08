import numpy as np

def main():
    edge_count = 0
    interior_count = 0
    with open('input.txt') as f:
        input = f.readlines()
        input = [[*x.strip('\n')] for x in input]
        input_np = np.array(input).astype(int)

        rows,cols = input_np.shape

        for row in range(rows):
            for col in range(cols):
                print(f'row {row}')
                print(f'col {col}')

                current_tree_height = input_np[row,col]
                print('current tree', current_tree_height)

                if row != 0 and col!= 0 and row != input_np.shape[0]-1 and \
                        col != input_np.shape[1]-1: #interior
                    print('interior')
                    if row-1 ==0:
                        tree_up = np.array([input_np[0, col]])
                    else:
                        tree_up = input_np[0:row, col]

                    if col-1 ==0:
                        tree_left = np.array([input_np[row, 0]])

                    else:
                        tree_left = input_np[row, 0:col]

                    if row+1 ==input_np.shape[0]-1:
                        tree_down = input_np[row+1:, col]
                    else:
                        tree_down = input_np[row+1:, col]

                    if col + 1 == input_np.shape[1] - 1:
                        tree_right = input_np[row, col+1:]
                    else:
                        tree_right = input_np[row, col+1:]

                    print(f'tree up', tree_up)
                    print(f'tree left', tree_left)
                    print(f'tree down', tree_down)
                    print(f'tree right', tree_right)

                    if all(current_tree_height > i for i in tree_up) or \
                        all(current_tree_height > i  for i in tree_left) or \
                        all(current_tree_height > i for i in tree_down) or \
                        all(current_tree_height > i for i in tree_right):
                        interior_count+=1


                else:
                    edge_count+=1
                    # print(f'edge_count', edge_count)

    print(edge_count)
    print(interior_count)
    print(edge_count+interior_count)





if __name__ == '__main__':
    main()

