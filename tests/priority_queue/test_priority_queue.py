import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing(capsys):
    queue_with_priority = PriorityQueue()
    priority_file = {
        'nome_do_arquivo': 'Indy',
        'qtd_linhas': 2,
        'linhas_do_arquivo': ['Indianapolis', '500']
    }
    normal_file = {
        'nome_do_arquivo': 'Le_Mans',
        'qtd_linhas': 5,
        'linhas_do_arquivo': ['24', 'horas', 'de', 'le', 'mans']
    }

    queue_with_priority.enqueue(priority_file)
    queue_with_priority.enqueue(normal_file)
    assert len(queue_with_priority) == 2

    assert queue_with_priority.search(0) == priority_file
    assert queue_with_priority.search(1) == normal_file
    with pytest.raises(IndexError, match='Índice Inválido ou Inexistente'):
        queue_with_priority.search(2)

    assert queue_with_priority.is_priority(normal_file) is False

    assert queue_with_priority.dequeue() == priority_file
    assert len(queue_with_priority) == 1
