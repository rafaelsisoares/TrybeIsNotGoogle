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


def exists_word(word, instance):
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


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
