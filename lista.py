def by_name(item):
    return item['nombre']

def by_hegiht(item):
    return item['altura']

def by_name2(item):
    if item['species'] is not None:
        return item['name'] +item['species']
    else:
        return item['name']
    
def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()

def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento['nombre'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['sublist']):
            print('    ', second_index, second_element)
    print()