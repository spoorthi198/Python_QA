# given array retun the indicies of two number which computes to target

class Summing:

  def two_Sum(self,nums,target):
      complements = {}
      result = []

      for index,num in enumerate(nums):
          if complements.get(num) is None:
              complements[target-num] = index
          else:
              result = [complements[num],index]
              break
      return result





l=Summing()
res = l.two_Sum([1,2,3,4],4)

res1=l.two_Sum([2,7,11,15],9)
res2=l.two_Sum([2,7,11,15],26)
#{24:0,19:1,15:2}
# 15 exists so res=[2,3]





print(res2)





