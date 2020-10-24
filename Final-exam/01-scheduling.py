def solve(jobs, target_index):
    number_at_target = jobs[target_index]
    cycles = 0

    while True:

        if not jobs:
            print(cycles)
            break

        fastest_job = min(jobs)

        if fastest_job <= number_at_target:
            cycles += fastest_job
            jobs.remove(fastest_job)
        else:
            print(cycles)
            break


jobs = [int(x) for x in input().split(", ")]
target_index = int(input())

solve(jobs, target_index)