DATA = {
    'ingredient__name': 'Название ингредиента',
    'amount': 'количество',
    'ingredient__measurement_unit': 'единица измерения'
}


def make_send_file(ingredient):
    with open('shop_list_file.txt', 'w') as shop_list_file:
        shop_list_file.write('Список ингредиентов:\n\n')
        for i in ingredient:
            for key, value in i.items():
                shop_list_file.write(f'{DATA[key]} - {value}\n')
                if key == 'amount':
                    shop_list_file.write('\n')

    with open('shop_list_file.txt', 'r') as f:
        file_data = f.read()
    return file_data
