import pandas as pd
import string


def split_text(content):
    n = int(len(content)/2)
    first = content[:n]
    sec = content[n:]

    fir = [*first]
    sec = [*sec]
    char = list(set(fir).intersection(sec))[0]


    alphabet_list = string.ascii_lowercase
    if char.isupper():
        index = alphabet_list.index(char.lower()) + 27
    else:
        index = alphabet_list.index(char) + 1

    return index


if __name__ == '__main__':
    df = pd.read_table('input.txt', delimiter='\n', header=None)
    df.columns = ['contents']
    df[['score']] = df['contents'].apply(
        lambda x: split_text(x))

    print(f'sum of the priorities: {df["score"].sum()}')