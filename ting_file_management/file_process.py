from ting_file_management.file_management import txt_importer

processed = set()


def process(path_file, instance):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return
    # solução desenvolvida com auxilio do Carlos Melo em mentoria. 

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
    if len(instance) == 0:
        print("Não há elementos")
        return

    info_to_remove = instance.dequeue()

    path_file = info_to_remove["nome_do_arquivo"]

    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
