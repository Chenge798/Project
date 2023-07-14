import random

# 生成30个1到50的随机整数
random_integers = [random.randint(1, 50) for _ in range(30)]

# 按照类别1-10，11-20，21-30，31-40，41-50进行分类
categories = [[], [], [], [], []]
for integer in random_integers:
    if integer <= 10:
        categories[0].append(integer)
    elif integer <= 20:
        categories[1].append(integer)
    elif integer <= 30:
        categories[2].append(integer)
    elif integer <= 40:
        categories[3].append(integer)
    else:
        categories[4].append(integer)

# 输出分类后每个类别的数据情况
for i, category in enumerate(categories):
    print(f"Category {i+1}: {category}")