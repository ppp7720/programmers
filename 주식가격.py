prices = [9,8,7,6,5,4,3,2,1,0]

from collections import deque

# r = []
# def count(a):
#     for i in range(len(prices[a:])):
#         if prices[a] > prices[a:][i]:
#             r.append(i)
#             return
#     r.append(len(prices)-a-1)
#     return

# for i in range(len(prices)):
#     count(i)

# def solution2(prices):

#     class price():
#         def __init__(self, prices, time):
#             self.p = prices
#             self.t = time

#     pp = deque(prices)
#     stack = []
#     r = []
#     timer = 1

#     p = price(pp[0], timer)
#     stack.append(p)
#     pp.popleft()
#     timer += 1

#     while pp:
#         while stack[-1].p > pp[0]:
#             r.append([p.t, timer-p.t])
#             stack.pop()
#         p = price(pp[0], timer)
#         stack.append(p)
#         pp.popleft()
#         timer += 1

#     result = sorted([[i.t, timer-i.t-1] for i in stack] + r)
#     return [i[1] for i in result]


# t = 1

# def go(s,p):
#         global t
#         s.append(p[0])
#         p.popleft()
#         t += 1

# def solution3(prices):
#     s, r = [], []
#     p = deque([[i+1, a] for i, a in enumerate(prices)])

#     go(s,p)
#     while p:
#         while s and s[-1][1] > p[0][1]:
#             r.append(s[-1]+[t-s[-1][0]])
#             s.pop()
#         go(s,p)
    
#     r += [i+[t-i[0]-1] for i in s]
#     r.sort()

#     return [i[2] for i in r]

# print(solution3(prices))

def solution4(prices):
    d = deque(prices)
    answer = []

    while d:
        l = d.popleft()
        c = 0
        
        for i in d:
            if l > i:
                c+=1
                break
            c+=1
        answer.append(c)
    
    return answer

print(solution4(prices))


# 주식가격
# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
# ※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.