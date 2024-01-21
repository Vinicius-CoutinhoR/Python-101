from datetime import datetime


class Task:
    def __init__(self, description=''):
        self.description = description
        self.done = False
        self.createdIn = datetime.now()

    def finish(self):
        self.done = True

    def __str__(self):
        return self.description + (' (Finished)' if self.done else '')


def main():
    house = []
    house.append(Task('Iron Clothes'))
    house.append(Task('Wash Dishes'))

    # Challenge -> Wash Dishes
    [task.finish() for task in house if task.description == 'Wash Dishes']
    for task in house:
        print(f'- {task}')


if __name__ == '__main__':
    main()
