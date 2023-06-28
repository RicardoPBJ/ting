import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance._data:
        if i['nome_do_arquivo'] == path_file:
            return

    importer = txt_importer(path_file)

    obj = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(importer),
        'linhas_do_arquivo': importer
    }

    instance.enqueue(obj)
    print(obj)


def remove(instance):
    if instance.is_empty():
        print('Não há elementos', file=sys.stdout)
        return
    result = instance.dequeue()["nome_do_arquivo"]
    print(f'Arquivo {result} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
