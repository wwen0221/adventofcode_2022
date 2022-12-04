import pandas as pd


def get_pairs(pairs):
    first = pairs.split(',')[0]
    first_min = int(first.split('-')[0])
    first_max = int(first.split('-')[1])
    second = pairs.split(',')[1]
    second_min = int(second.split('-')[0])
    second_max = int(second.split('-')[1])

    if (second_min >= first_min  and second_min <= first_max) and \
        (second_max >= first_min  and second_max <= first_max):
        return 1
    elif (first_min >= second_min  and first_min <= second_max) and \
        (first_max >= second_min  and first_max <= second_max):
        return 1
    else:
        return 0


if __name__ == '__main__':
    df = pd.read_table('input.txt', delimiter='\n', header=None)
    df.columns = ['pairs']
    df['is_within'] = df['pairs'].apply(lambda x: get_pairs(x))

    print(df['is_within'].sum())
