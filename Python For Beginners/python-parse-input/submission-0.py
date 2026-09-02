from typing import List

def read_integers() -> List[int]:
    msg = input()
    integer_list = msg.split(",")
    result = []

    for char in integer_list:
        result.append(int(char))
    
    return result


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
