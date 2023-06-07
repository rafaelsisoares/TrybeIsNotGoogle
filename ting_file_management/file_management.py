import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido')
    try:
        with open(path_file, mode='r') as file:
            return [line.strip('\n') for line in file]
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
