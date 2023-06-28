import sys


def txt_importer(path_file: str) -> list:
    if '.txt' not in path_file:
        print('Formato inválido', file=sys.stderr)
        return

    try:
        with open(path_file, 'r') as file:
            return file.read().splitlines()

    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
        return
