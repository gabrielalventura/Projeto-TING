def exists_word(word, instance):
    existents = []
    word_lower = word.lower()
    for i in range(len(instance)):
        info = instance.search(i)
        word_info = {
            "palavra": word,
            "arquivo": info["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for i, line in enumerate(info["linhas_do_arquivo"], start=1):
            line_lower = line.lower()
            if word_lower in line_lower:
                word_info["ocorrencias"].append({"linha": i})
        if word_info["ocorrencias"]:
            existents.append(word_info)
    return existents


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
