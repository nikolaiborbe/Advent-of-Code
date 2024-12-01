def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        left_list, right_list = [], []
        for line in lines:
            left, right = map(int, line.split())  
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def calc(l1, l2):
    pass

def main():
    file_name = 'input.txt'
    l1, l2 = read_input(file_name)
    output = calc(l1, l2)
    print(output)

if __name__ == "__main__":
    main()