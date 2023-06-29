
def exists_word(word: str, instance):
    result = list()
    for i in range(len(instance)):
        search = instance.search(i)
        lines_searched = [
            {"linha": index + 1}
            for index, line in enumerate(search['linhas_do_arquivo'])
            if word.lower() in line.lower()
        ]

        if lines_searched:
            obj = {
                "palavra": word,
                "arquivo": search["nome_do_arquivo"],
                "ocorrencias": lines_searched
            }
            result.append(obj)

    return result


def search_by_word(word, instance):
    result = list()
    for i in range(len(instance)):
        search = instance.search(i)
        lines_searched = [
            {"linha": index + 1, "conteudo": line}
            for index, line in enumerate(search['linhas_do_arquivo'])
            if word.lower() in line.lower()
        ]

        if lines_searched:
            obj = {
                "palavra": word,
                "arquivo": search["nome_do_arquivo"],
                "ocorrencias": lines_searched
            }
            result.append(obj)

    return result
