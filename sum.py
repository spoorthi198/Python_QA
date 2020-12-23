class Summing:
    def twosum(self, nums,target):
        compliments = {}
        result = []

        for index, num in enumerate(nums):
            if compliments.get(num) is None:
                compliments[target-num] = index
            else:
                result =[compliments[num],index]
                break
        return result


l=Summing()
#res = l.twosum([1,2,3,4],4)

res=l.twosum([2,7,11,15],9)
res1=l.twosum([2,7,11,15],26)
#{24:0,19:1,15:2}
# 15 exists so res=[2,3]





print(res1)





