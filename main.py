for i in range(100):
    with open(f'files/main_0{i}.txt', 'w') as file:
        file.write(f'Это файл #{i}')