def main():

    d = {}

    with open('input.txt') as f:
        input = f.readlines()
        parent_dir = 'main'
        d[parent_dir] = 0
        for command in input[1:]:
            if '$ ls' not in command:
                if 'cd ' not in command:
                    if 'dir ' in command:
                        child_dir = command.split('dir')[-1].strip()
                        temp_path = f'{parent_dir}/{child_dir}'
                        if temp_path not in d.keys():
                            d[temp_path]=0

                    else: #is a file
                        child_size = int(command.split(' ')[0].strip())
                        d[parent_dir] += child_size
                        if len(parent_dir.split('/'))>1:
                            #update parent dir
                            temp_parent_dir = parent_dir
                            while temp_parent_dir !='main':
                                temp_parent_dir = temp_parent_dir.rsplit('/',1)[0]
                                d[temp_parent_dir]+=child_size

                else:#update dir
                    if '..' not in command:
                        child_dir = command.split('cd ')[-1].strip()
                        parent_dir=f'{parent_dir}/{child_dir}'

                    if '..' in command:
                        parent_dir = parent_dir.rsplit('/',1)[0]

    sum_list = []
    for dir, size in d.items():
        if size < 100000:
            sum_list.append(size)

    print(sum(sum_list))


if __name__ == '__main__':
    main()