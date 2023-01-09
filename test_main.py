from main import square_eq_solver, show_result


def test_no_root():
    res = square_eq_solver(10, 0, 2)
    assert len(res) == 0


def test_single_root():
    res = square_eq_solver(10, 0, 0)
    assert len(res) == 1
    assert res == [0]


def test_multiple_root():
    res = square_eq_solver(2, 5, -3)
    assert len(res) == 3
    assert res == [0.5, -3]

def test_empty_result(capsys):
    show_result([])
    captured = capsys.readouterr()
    assert captured.out == 'Уравнение с заданными параметрами не имеет корней\n'

def test_non_empty_result(capsys):
    show_result([0.5, -3])
    captured = capsys.readouterr()
    assert captured.out == 'Корень номер 1 равен 0.50\nКорень номер 2 равен -3.00\n'

