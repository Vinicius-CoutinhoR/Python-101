class Human:
    # Class Attribute
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def caveman(self):
        self.specie = 'Homo Neanderthalensis'


if __name__ == '__main__':
    joseph = Human('joseph')
    grokn = Human('Grokn')
    grokn.caveman()

    print(f'Human Specie: {Human.specie}')
