from app.utils.generator import newName
from app.business import nameExists
from app.business.backend import addName


def main():
    while True:
        name = newName()
        if not nameExists(name):
            addName(name)
            break
    print(f'Created new test name! {name}')


main()
