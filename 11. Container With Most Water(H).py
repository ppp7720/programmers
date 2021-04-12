height = [1,8,6,2,5,4,8,3,7]
s = 0
for n in set(height):
    l, r = 0, 0
    for i in range(len(height)):
        if height[i] >= n:
            l = i
            break
    for j in range(len(height)-1,0,-1):
        if height[j] >= n:
            r = j
            break
    if (r-l)*n >= s:
        s = (r-l)*n

print(s)