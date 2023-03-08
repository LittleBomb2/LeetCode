nums = [0, 1, 3, 7, 8]
target = 4

class Solution:
  def __init__(self):
    self.numerolista = []
    self.tulos = 0

  def twoSum(self, lista, summa):
    for x in lista:
      for y in lista:
        if x + y == summa and lista.index(x) != lista.index(y):
          return [lista.index(x), lista.index(y)]
          
    self.numerolista = lista
    
    
ratkaisu = Solution()

lopullinen_vastaus = ratkaisu.twoSum(nums, target)
print(lopullinen_vastaus)