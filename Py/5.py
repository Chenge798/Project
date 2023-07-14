print("\t通信2113班歌咏比赛打分程序")
print("===========================================")
print("请输入 7 名裁判的打分,用英文逗号间隔分数 ：")
scores = list(map(int, input().split(',')))

# 找到最大值
big_score = max(scores)
small_score = min(scores)

# 去掉一个最低分和一个最高分
scores.sort()
scores = scores[1:-1]
11
# 输出该选手的得分（平均分）和最大值
average_score = sum(scores) / len(scores)
print("去掉一个最低分:", small_score)
print("去掉一个最高分:", big_score)
print(f'该选手的得分为：{average_score:.2f}分')