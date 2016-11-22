class Optimizer:
    __costs = []
    __teams_max = 0
    __works_max = 0

    def __init__(self, filename):
        with open(filename) as file:
            wt = file.readline()

            self.__works_max, self.__teams_max = tuple(map(int, wt.split()))
            self.__costs = [[int(num) for num in line.split()] for line in file.readlines()]

    def human_best(self):
        schedule = {team_id: [] for team_id in range(self.__teams_max)}

        for work in range(self.__works_max):
            min_len = len(min(schedule.values(), key=lambda value: len(value)))

            ct = [key for key, value in schedule.items() if len(value) == min_len]

            best_team = min(ct, key=lambda team_id: self.__costs[team_id][work])

            schedule[best_team].append(work)

        return schedule


def main():
    optimizer = Optimizer('w500t10.txt')

    print(optimizer.human_best())


if __name__ == '__main__':
    main()
