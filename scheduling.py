import random
import copy

import annealing


class SchedulingProblem:
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

    def cost(self, schedule):
        r = sum([
                    self.__costs[team_id][work_id] for team_id, work_id in
                    [(team_id, work_id) for team_id, value in schedule.items() for work_id in value]
                    ])
        return r

    def random_schedule(self):
        schedule = {team_id: [] for team_id in range(self.__teams_max)}

        for work_id in range(self.__works_max):
            team_id = random.randint(0, self.__teams_max - 1)
            schedule[team_id].append(work_id)

        return schedule

    def neighbour_schedule(self, base):

        schedule = copy.deepcopy(base)

        return schedule


def temperature():
    t = 10

    while t > 0:
        yield t
        t -= 0.001


def main():
    problem = SchedulingProblem('w500t10.txt')

    annealing.funcs['temperature'] = temperature
    annealing.funcs['energy'] = problem.cost
    annealing.funcs['random_state'] = problem.random_schedule
    annealing.funcs['next_state'] = problem.neighbour_schedule

    human = problem.cost(problem.human_best())
    best = problem.cost(annealing.optimize())

    print('human: {0}'.format(human))
    print('annealing: {0}'.format(best))


if __name__ == '__main__':
    main()
