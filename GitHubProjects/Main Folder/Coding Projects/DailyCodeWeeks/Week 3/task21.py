MAX = 100001

def minHalls(lectures, n):
 
    prefix_sum = [0] * MAX

    for i in range(n) :
        prefix_sum[lectures[i][0]] += 1
        prefix_sum[lectures[i][1] + 1] -= 1
         
    ans = prefix_sum[0]

    for i in range(1, MAX) :
        prefix_sum[i] += prefix_sum[i - 1]
        ans = max(ans, prefix_sum[i])
         
    return ans

if __name__ == "__main__" :
 
    lectures = [[0, 5], [1, 2], [1, 10]]      
    n = len(lectures)
    print(minHalls(lectures, n))