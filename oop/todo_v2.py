from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def add(self, description, overdue=None):
        self.tasks.append(Task(description, overdue))

    def pendings(self):
        return [task for task in self.tasks if not task.done]

    def find(self, description):
        return [task for task in self.tasks
                if task.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.pendings())} pending task(s))'


class Task:
    def __init__(self, description='', overdue=None):
        self.description = description
        self.done = False
        self.createdIn = datetime.now()
        self.overdue = overdue

    def finish(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append('(Finished)')
        elif self.overdue:
            if datetime.now() > self.overdue:
                status.append('(Overdue)')
            else:
                day = (self.overdue - datetime.now()).days
                status.append(f'(Overdue in {day} day(s))')


class RoutineTask(Task):
    def __init__(self, description, overdue, days=7):
        super().__init__(description, overdue)
        self.days = days

    def finish(self):
        super().finish()
        new_overdue = datetime.now() + timedelta(days=self.days)
        return RoutineTask(self.description, new_overdue. self.days)


def main():
    house = Project('House tasks')
    house.add('Iron Clothes', datetime.now())
    house.add('Wash Dishes', datetime.now() + timedelta(days=3, minutes=12))
    house.tasks.append(RoutineTask('Change clothes', datetime.now(), 7))
    print(house)
    # Challenge -> Wash Dishes

    house.find('Wash Dishes').finish()
    for task in house:
        print(f'- {task}')
    print(house)


if __name__ == '__main__':
    main()
