# coding=utf-8

"""
给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
"""

# Number of layer to rotate is n//2. For each item along the top side of each layer, save as temp and 
# move in the item from the next side, repeating until temp is put into the last side. 
# Alternatively - matrix[:] = list(map(list, zip(*matrix[::-1]))). 
# Reverse the order of row, unpack, # zip and convert back to lists.


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layers = n//2

        for layer in range(layers):
            for i in range(layer, n - layer - 1):
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[n - 1 - i][layer]
                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1 - i]
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                matrix[i][n - 1 - layer] = temp
        return matrix


# 方法二更优，代码更简洁，执行时间更短
class SolutionSolution(object):
    def rotaterotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.         :ty 
        """
        matrix.reverse()
        # zip函数用于将可迭代的对象做为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        matrix_tmp = zip(*matrix)  # 妙啊
        for i in range(len(matrix)):
            matrix[i] = list(matrix_tmp[i])
        return matrix


matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

a = Solution()
print a.rotate(matrix)