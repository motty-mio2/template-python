from template_python import common as c


def test_echo() -> None:
    assert c.echo() == "Hello"


def test_echo_word() -> None:
    word: str = "test"
    assert c.echo(txt=word) == word
