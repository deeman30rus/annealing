import random

MAX_VERTICES = 100


def gen_schedule_costs():
    WORKS_MAX = 10000
    TEAMS_MAX = 100

    WORKS_COST_RANGE = (500, 1000)
    TEAMS_SKILL_RANGE = (0, 50)

    RANDOM_FACTOR_RANGE = (0, 10)

    with open("w{0}t{1}.txt".format(WORKS_MAX, TEAMS_MAX), 'w') as file:
        file.write("{0} {1}\n".format(WORKS_MAX, TEAMS_MAX))

        works = [random.randint(*WORKS_COST_RANGE) for w in range(WORKS_MAX)]
        teams = [random.randint(*TEAMS_SKILL_RANGE) for t in range(TEAMS_MAX)]

        file.write(
            '\n'.join(
                [' '.join(
                        [str(work_cost - team_skill + random.randint(*RANDOM_FACTOR_RANGE)) for work_cost in works]
                ) for team_skill in teams]
            )
        )


def gen_tsp():
    max = 20

    for i in range(max):
        with(open("input-{0}.txt".format(i), 'w')) as file:
            file.write('\n'.join([' '.join([str(random.randint(0, 1000)) for y in range(0, MAX_VERTICES)]) for x in
                                  range(0, MAX_VERTICES)]))


def main():
    gen_schedule_costs()


if __name__ == '__main__':
    main()
