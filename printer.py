def print_array(array: list) -> None:
    for element in array:
        if isinstance(element, dict):
            print_dict(element)
        else:
            print(element)

        print('-------')

def print_dict(d: dict) -> None:
    for key, value in d.items():
        print(f'{key}: {value}')
