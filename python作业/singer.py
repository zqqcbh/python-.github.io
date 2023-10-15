# # 青春有你
candidate_names = ["虞书欣","刘雨欣","喻言","许佳琪","孙芮","莫寒","宋昕冉","费沁源"]
candidate_no = [i+1 for i,j in enumerate(candidate_names)]
#
# # for i in range(1,len(candidate_names)+1):
# #     candidate_no.append(i)
#
# #分配选手编号
# #创建一个{姓名:编号}字典
name_no = {}
for name,no in zip(candidate_names,candidate_no):
    name_no[name] = no
print(name_no)
#
# # 生成票数
import random
votes = []
for i in range(2000):
    vote = random.choice(list(name_no.values()))
    votes.append(vote)
# print(votes)
#
# # 统计票数
no_votes = {}
for i in votes: # votes=[1,2,1,3,1]
    if i not in no_votes.keys():
        no_votes[i] = 1
    else:
        no_votes[i] += 1
print(no_votes)

#{姓名:票数}字典建立
name_votes = {p:j for i,j in no_votes.items() for p,q in name_no.items() if i==q}
print(name_votes)
#
# # 字典排序
final_result = sorted(name_votes.items(),key=lambda x:x[1],reverse=True)
print(final_result)
#
# # 不用字典排序
# candidate_votes = list(name_votes.values())
# candidate_votes.sort(reverse=True)
#
# votes_name = {j:i for i,j in name_votes.items()}
# print("最终淘汰的选手是：{},{}".format(votes_name[candidate_votes[-1]],votes_name[candidate_votes[-2]]))
# #
# # # 淘汰
print("最终淘汰的选手是：{},{}".format(final_result[-1][0],final_result[-2][0]))