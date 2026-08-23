from opswatch import main


def test_main_exist() -> None:
    assert callable(main)
