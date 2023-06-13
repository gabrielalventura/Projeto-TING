from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    processed = set()

    if path_file in processed:
        return

    txt = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }

    instance.enqueue(dict)  # adiciona dict na fila

    processed.add(path_file)
    # adiciona o arquivo ao conjunto de arquivos processados

    print(dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
