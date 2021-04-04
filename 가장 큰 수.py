from itertools import permutations

nums = [6, 10, 2]

def solution(n):
    n = list(map(str,n))[::-1]
    
    return 
# p = list(permutations(n,len(n)))

# print(solution(nums))

n = sorted(list(map(str,nums)), reverse=1)
for i in range(len(n)-1):
    if n[i]+n[i+1] < n[i+1]+n[i]:
        n[i], n[i+1] = n[i+1], n[i]
print(n)