def process_info(word, lines, is_full_info):
    info = []
    for i in range(len(lines)):
        if word.lower() in lines[i].lower():
            if is_full_info:
                info.append({
                    'linha': i + 1,
                    'conteudo': lines[i],
                })
            info.append({'linha': i + 1})

    return info


def formater(word, instance, is_full_info):
    results = []
    for i in range(len(instance)):
        info = process_info(
            word,
            instance.search(i)['linhas_do_arquivo'],
            False
        )
        if info:
            results.append({
                'palavra': word,
                'arquivo': instance.search(i)['nome_do_arquivo'],
                'ocorrencias': info
            })
    return results


def exists_word(word, instance):
    return formater(word, instance, False)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
