from template_python.common import func as f


def test_echo() -> None:
    assert f.echo() == "Hello"


def test_echo_word() -> None:
    word: str = "test"
    assert f.echo(txt=word) == word
