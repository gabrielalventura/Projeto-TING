import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
        return
    try:
        with open(path_file, 'r') as file:
            txt = file.read().split('\n')
            return txt
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
        return

# referencia endswith:
# https://www.w3schools.com/python/ref_string_endswith.asp
# e consulta material seção 01 do módulo de Ciências da Computação
