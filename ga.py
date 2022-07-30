# 試行回数
#EPISODE_NUMB = 1

GEN_MAX = 15 # 世代交代数
POP_SIZE = 20 # 個体数（個体群のサイズ）= M
MUTATE_PROB = 0.05 # 突然変異率
ELITE = 2

N = 3000 # 各個体における染色体の次元数

# 遺伝子作成
def create_gene():
    generation = []
    for x in range(POP_SIZE):
        gene = []
        for y in range(N):
            gene.append(random.choice([0, 1]))
        generation.append(gene)
    return generation

# 2点交叉
def two_crossover(parent0, parent1):

    child = []

    point1 = random.randint(0, N-1)
    point2 = (point1 + (random.randint(0, N-2)+1))%(N-1)

    if point1 > point2:
        tmp = point1
        point1 = point2
        point2 = tmp

    for i in range(point1+1):
        child.append(parent0[i]) 
    
    for j in range(point1+1, point2):
        child.append(parent1[j])
    
    for k in range(point2, N):
        child.append(parent0[k])

    return child


# 遺伝子のスコアによるソート
def sorts_gene(genes, scores):
    sorted_index = np.argsort(scores)[::-1]
    sorted_li = []
    for x in sorted_index:
        sorted_li.append(genes[x])
    
    return sorted_li

# 順位に基くランキング選択
def select():
    
    denom = 10 * (10 + 1) / 2
    r = random.randint(1,denom)
    for num in range(10,0,-1):
        if(r <= num):
            break
        r -= num 
    return 10 - num
    

def mutate(chrom):

    mutated_copy = copy.deepcopy(chrom)   
    
    for index in range(N):
        RAND_01 = random.random()
        if RAND_01 < MUTATE_PROB:
            if mutated_copy[index] == 0:
                mutated_copy[index] = 1
            else:
                mutated_copy[index] = 0                                     

    return mutated_copy
