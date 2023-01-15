from faker import Faker


def echo(txt: str = "Hello") -> str:
    return txt


def person() -> str:
    fake = Faker("jp-JP")
    name: str = fake.name()
    return name
