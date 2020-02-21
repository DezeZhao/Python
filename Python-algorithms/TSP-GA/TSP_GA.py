import random
import re
from sys import float_info

import matplotlib.pyplot as plt

# population size
POPSIZE = 50

# probability of crosscover
PCROSSOVER = 0.9

# probability of mutation
PMUTATION = 0.2

# max number of generations
MAXGENS = 1000  # 最大迭代次数

CROSSGENE = 0

# dist
dist = []


class city:
    def __init__(self, cityName, x, y):
        self.cityName = cityName
        self.x = x
        self.y = y


def read_tsp(filename):
    """
    Read a file in .tsp format into a pandas DataFrame
    """
    with open(filename) as file:
        cities = []
        flag = False
        for line in file.readlines()[0:-1]:
            if line.startswith('EOF'):
                break
            if line.startswith('NODE_COORD_SECTION'):
                flag = True
            elif flag:
                info = re.split('[ ]+', line.strip())
                cities.append(city(info[0], float(info[1]), float(info[2])))

        # check cities
        # for i in range(len(cities)) :
        #     print(cities[i].x, cities[i].y)
    return cities


# Initial population
def initPopulation(cities, numOfCity):
    population = []

    # 随机洗牌  随机排序0~numOfCity-1
    individual = [i for i in range(numOfCity)]
    for _ in range(int(POPSIZE * 2 / 10)):
        random.shuffle(individual)  # 循环生成序列
        population.append(individual[:])  # 加入到种群里面

    # 贪心策略
    for _ in range(int(POPSIZE - len(population))):
        begin = random.randint(0, numOfCity - 1)
        gIndividual = [begin]
        j = 1
        while j < numOfCity:  # 选一个与当前gIndividual最后一个城市相距最近的一个城市
            mixDis = float_info.max
            i, bestId = 0, 0
            while i < numOfCity:
                if (i not in gIndividual) and i != gIndividual[-1] and dist[gIndividual[-1]][i] < mixDis:
                    bestId = i
                    mixDis = dist[gIndividual[-1]][i]
                i += 1
            j = j + 1
            gIndividual.append(bestId)
        population.append(gIndividual)

    random.shuffle(population)
    return population


# calculate indibidual fitness
def evaluate(individual):
    fitness = 0.0
    len_ = len(individual)
    for i in range(len_ - 1):
        fitness += dist[individual[i]][individual[i + 1]]
    # back to starting point
    fitness += dist[individual[len_ - 1]][individual[0]]
    return fitness


# selection operation
def select(population, numOfCity):
    newPopulation = []
    best = float_info.max  # 浮点数最大值from sys.float_info
    bestId = 0
    fitness = []
    sumOfFitness = 0.0

    # evalute
    for i in range(POPSIZE):
        fit = evaluate(population[i])
        fitness.append(1 / fit)
        sumOfFitness += 1 / fit
        if best > fit:
            best = fit
            bestId = i

    # choosing the best individual to directly inherit to the next generation
    newPopulation.append(population[bestId])

    # cumulative probability 累积概率
    cumPro = []
    for i in range(POPSIZE):
        if i == 0:
            cumPro.append(fitness[i] / sumOfFitness)
        else:
            cumPro.append(fitness[i] / sumOfFitness + cumPro[i - 1])

    # roulette selection of offspring 后代轮盘选择
    for i in range(POPSIZE - 1):
        pro = random.random()
        for j in range(POPSIZE):
            if cumPro[j] >= pro:
                newPopulation.append(population[j])
                break
    return newPopulation  # 选择的新的N个后代


def orderCross(idx_ge, chromo, idx_ch, begin, end):
    gene = chromo[idx_ch][idx_ge]
    if gene not in chromo[int(not idx_ch)][begin:end]:
        global CROSSGENE
        CROSSGENE = gene
        return
    idx_ch = int(not idx_ch)
    idx_ge = chromo[idx_ch].index(gene)
    orderCross(idx_ge, chromo, int(not idx_ch), begin, end)


# 有一定的概率进行交叉,此处采用次序交叉法——order crossover
def crossover(population, numOfCity):
    # order crossover
    subPopulation = []
    for i in range(POPSIZE):
        if random.random() <= PCROSSOVER:
            chromo1 = random.randint(0, POPSIZE - 1)
            chromo2 = random.randint(0, POPSIZE - 1)
            while chromo1 == chromo2:
                chromo2 = random.randint(0, POPSIZE - 1)
            chromo = [population[chromo1], population[chromo2]]
            begin = random.randint(0, numOfCity - 2)  # 染色体切割起始点
            end = random.randint(begin + 1, numOfCity - 1)  # 染色体切割终止点
            # begin = 4
            # end = 9
            newIndividual1 = [0] * numOfCity
            newIndividual2 = [0] * numOfCity
            k = 0
            for j in range(numOfCity):
                if begin <= j < end:
                    newIndividual1[begin:end] = population[chromo2][begin:end]  # 中间部分的基因直接复制即可
                    j = end
                else:
                    orderCross(j, chromo, 0, begin, end)
                    newIndividual1[j] = CROSSGENE

            for j in range(numOfCity):
                if begin <= j < end:
                    newIndividual2[begin:end] = population[chromo1][begin:end]
                else:
                    orderCross(j, chromo, 1, begin, end)
                    newIndividual2[j] = CROSSGENE

            subPopulation.append(newIndividual1)
            subPopulation.append(newIndividual2)
    # competition with population
    subPopulation.sort(key=lambda x: evaluate(x))
    for i in range(len(subPopulation)):
        for j in range(POPSIZE):
            if evaluate(subPopulation[i]) < evaluate(subPopulation[j]):
                population[j] = subPopulation[i]
                break

    return population


# mutation operation 倒置交叉法
def mutate(population, numOfCity):
    for i in range(len(population)):
        if random.random() <= PMUTATION:
            begin = random.randint(1, numOfCity - 2)
            end = random.randint(begin + 1, numOfCity - 1)
            population[i][begin:end] = population[i][end - 1:begin - 1:-1]
    return population


# local search 局部搜索
def localSearch(population, numOfCity):
    for i in range(len(population)):
        best = population[i][:]  # 不可缺少[:]
        for _ in range(100):
            begin = random.randint(1, numOfCity - 2)
            end = random.randint(begin + 1, numOfCity - 1)
            population[i][begin:end] = population[i][end - 1:begin - 1:-1]
            if evaluate(best) > evaluate(population[i]):
                best = population[i][:]  # 不可为population[i]否则画图不对
        population[i] = best
    return population


def main():
    cities = read_tsp("att48.tsp")
    x = []
    y = []
    # the num of city
    numOfCity = len(cities)

    # Calculate the Euclidean dist between cities
    for i in range(len(cities)):
        node = []
        for j in range(len(cities)):
            d = int(((cities[i].x - cities[j].x) ** 2 + (cities[i].y - cities[j].y) ** 2) ** 0.5 + 0.5)
            node.append(d)
        dist.append(node)

    population = initPopulation(cities, numOfCity)

    gen = 0
    while gen < MAXGENS:
        random.shuffle(population)
        population = select(population, numOfCity)
        population = crossover(population, numOfCity)
        population = mutate(population, numOfCity)
        population = localSearch(population, numOfCity)

        population.sort(key=lambda x: evaluate(x))
        print("generation: ", gen)

        plt.clf()

        fig1 = plt.figure(1)
        x = [i for i in range(gen + 1)]
        y.append(evaluate(population[0]))
        plt.plot(x, y, 'b--')

        fig2 = plt.figure(2)
        ax = plt.axes()
        ax.set_title('Distance: ' + str(evaluate(population[0])))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        for n in range(numOfCity - 1):
            plt.plot([cities[population[0][n]].x, cities[population[0][n + 1]].x],
                     [cities[population[0][n]].y, cities[population[0][n + 1]].y], '-go')
        plt.plot([cities[population[0][-1]].x, cities[population[0][0]].x],
                 [cities[population[0][-1]].y, cities[population[0][0]].y], '-go')

        plt.pause(0.0001)

        gen += 1

    # find best
    population[0].append(population[0][0])
    print(population[0])
    print(evaluate(population[0]))
    plt.clf()
    ax = plt.axes()
    ax.set_title('Distance: ' + str(evaluate(population[0])))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for n in range(numOfCity - 1):
        plt.plot([cities[population[0][n]].x, cities[population[0][n + 1]].x],
                 [cities[population[0][n]].y, cities[population[0][n + 1]].y], '-ro')
    plt.plot([cities[population[0][-1]].x, cities[population[0][0]].x],
             [cities[population[0][-1]].y, cities[population[0][0]].y], '-ro')

    plt.show()


if __name__ == "__main__":
    main()
