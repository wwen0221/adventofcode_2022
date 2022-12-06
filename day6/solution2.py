
def main():
    with open('input.txt') as f:
        input = f.read()
        length = len(input)

        start = 0
        end = 14
        while end != length:
            signal = input[start:end]
            start+=1
            end+=1
            if len(signal) == len(set(signal)):
                print(signal)
                print(end-1)

                break
if __name__ == '__main__':
    main()
