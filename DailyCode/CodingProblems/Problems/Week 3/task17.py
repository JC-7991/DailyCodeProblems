class Solution(object):

    def longestPath(self, input):

        max = 0
        path = {0: 0}

        for line in input.split('\n'):

            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name:
                max = max(max, path[depth] + len(name))

            else:
                path[depth + 1] = path[depth] + len(name) + 1

        return max