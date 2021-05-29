import random
def problem(x,y,z):
    return 10*x**3+9*y**2+90*z-69

def fitness(x,y,z):
    ans = problem(x,y,z)

    if ans == 0:
        return 9999
    else:
        return abs(1/ans)

#generating solutions

solution_set  = []
for num in range(1000):
    solution_set.append((random.uniform(0,1000),random.uniform(0,1000),random.uniform(0,1000)))

for i in range(10000):

    ranked_sol_set = []
    for num in solution_set:
        ranked_sol_set.append((fitness(num[0],num[1],num[2]),num ))
    ranked_sol_set.sort(reverse=True)

    print(f"===Gen{i} best solutions ===")
    print(ranked_sol_set[0])

    if ranked_sol_set[0][0] > 999:
        break

    bestsolutions = ranked_sol_set[:100]

    elements = []

    for num in bestsolutions:
        elements.append(num[1][0])
        elements.append(num[1][1])
        elements.append(num[1][2])

    new_gen = []
    for _ in range(1000):
        e1 = random.choice(elements)*random.uniform(0.99,1.01)
        e2 = random.choice(elements)*random.uniform(0.99,1.01)
        e3 = random.choice(elements)*random.uniform(0.99,1.01)

        new_gen.append((e1,e2,e3))

    solution_set = new_gen
