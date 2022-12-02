import pandas as pd

#convert
convert = {'A':'Rock','B':'Paper','C':'Scissors','X':'Rock','Y':'Paper',
           'Z':'Scissors'}


def get_correct_shape(combination):
    rules = {'Scissors,X': 'Paper',
             'Scissors,Z': 'Rock',
             'Scissors,Y': 'Scissors',
             'Paper,Y': 'Paper',
             'Paper,X': 'Rock',
             'Paper,Z': 'Scissors',
             'Rock,Z': 'Paper',
             'Rock,Y': 'Rock',
             'Rock,X': 'Scissors'
             }

    return rules[combination]

def calculate(combination):
    rules = {'Scissors,Paper': 'lose',
             'Scissors,Rock': 'win',
             'Scissors,Scissors': 'draw',
             'Paper,Paper': 'draw',
             'Paper,Rock': 'lose',
             'Paper,Scissors': 'win',
             'Rock,Paper': 'win',
             'Rock,Rock': 'draw',
             'Rock,Scissors': 'lose'
             }

    score = {'Rock':1,'Paper':2,'Scissors':3}

    result = rules[combination]
    shape_score = score[combination.split(',')[-1]]

    if result == 'win':
        return 6+shape_score
    elif result == 'draw':
        return 3+shape_score
    else:
        return 0+shape_score


if __name__ == '__main__':
    df = pd.read_table('input.txt', delimiter=' ',header=None)
    df.columns = ['opponent','me']
    df['oppo_converted'] = df['opponent'].apply(lambda x: convert[x])
    df['me_converted'] = df['me'].apply(lambda x: convert[x])
    df['combination'] = df[['oppo_converted','me']].apply(
        lambda x: ','.join(x),axis=1)
    df['what_to_choose'] = df['combination'].apply(lambda x: get_correct_shape(x))

    df['new_combination'] = df[['oppo_converted','what_to_choose']].apply(
        lambda x: ','.join(x),axis=1)
    df['score'] = df['new_combination'].apply(lambda x: calculate(x))
    print(df)

    #part 1 ans
    # df['combination'] = df[['oppo_converted','me_converted']].apply(
    #     lambda x: ','.join(x),axis=1)
    # df['score'] = df['combination'].apply(lambda x: calculate(x))

    print(df['score'].sum())

