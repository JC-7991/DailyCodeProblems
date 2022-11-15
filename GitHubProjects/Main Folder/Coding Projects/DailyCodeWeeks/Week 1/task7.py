import string 

dmap = dict(
    zip(range(1, 27), string.ascii_lowercase)
)

class Solution:
    
    def solve(self, message):

        arr = [0] * len(message)
        arr[-1] = 1

        if len(message) > 1:
            arr[-2] = 2 if int(message[-2:]) in dmap else 1

        for i in reversed(range(len(message) - 2)):
            into = int(message[i:i + 2]) in dmap
            arr[i] = arr[i + 1] + (arr[i + 2] if into else 0)
        
        return arr[0]