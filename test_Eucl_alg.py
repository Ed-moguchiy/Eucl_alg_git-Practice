import Eucl_alg


def test_nod(func):
    # -- тест 1 ---------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('#test 1 - of')
    else:
        print('#test 1 - fail')


# -- тест 2 ---------------

    a = 100
    b = 1
    res = func(a, b)

    if res == 1:
        print('#test 2 - ok')
    else:
        print('#test 2 - fail')


test_nod(Eucl_alg.get_nod)
