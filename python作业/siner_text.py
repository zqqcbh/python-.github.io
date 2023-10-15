singers_name =['克莱恩','奥黛丽','阿尔杰','威尔','乌洛琉斯','卢米安','芙兰卡','卡夫卡']
singer_no = [i+1 for i,j in enumerate(singers_name)]
#排号
singer_ifo = {}
ifo = zip(singers_name,singer_no)
for i,j in ifo:
    singer_ifo[i] = j
print(singer_ifo)
#集票
import random
votes = []
for i in range(2000):
    vote = random.choice(list(singer_ifo.values()))
    votes.append(vote)
# print(votes)
#统计票数
vote_avg = {}
for i in votes:
    if i not in vote_avg.keys():
        vote_avg[i] = 1
    else:
        vote_avg[i] += 1
print(vote_avg)
#整合
singer_votes = {p:j for p,q in singer_ifo.items() for i,j in vote_avg.items() if q == i}
print(singer_votes)
#字典排序
final_ifo = sorted(singer_votes,key=lambda x:x[0],reverse=True)
#不用字典排序
# no_avg = [i for i in singer_votes.values()]
# no_avg.sort(reverse=True)
# name = {i:j for j,i in singer_votes.items()}
# print(no_avg)
# print("被淘汰的选手是: {},{}".format(name[no_avg[-1]],name[no_avg[-2]]))
#用字典排序收尾
print("被淘汰的选手是: {} {}".format(final_ifo[-1][2],final_ifo[-2][]))











