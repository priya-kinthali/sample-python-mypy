def foo() -> str:
    return 1


def foo2() -> str:
    return foo() + "foo"
