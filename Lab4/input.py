FILE_IN = "input.txt"


def getdata_file():
    data = {'dots': []}

    with open(FILE_IN, 'rt', encoding='UTF-8') as fin:
        try:
            for line in fin:
                current_dot = tuple(map(float, line.strip().split()))
                if len(current_dot) != 2:
                    raise ValueError
                data['dots'].append(current_dot)
            if len(data['dots']) < 2:
                raise AttributeError
        except (ValueError, AttributeError):
            return None

    return data
