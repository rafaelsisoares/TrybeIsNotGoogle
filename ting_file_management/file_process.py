from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    file_processed = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }
    for i in range(len(instance)):
        if instance.search(i) == file_processed:
            return
    instance.enqueue(file_processed)
    print(file_processed)


def remove(instance):
    try:
        file = instance.dequeue()['nome_do_arquivo']
        print(f'Arquivo {file} removido com sucesso')
    except IndexError:
        print('Não há elementos')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
