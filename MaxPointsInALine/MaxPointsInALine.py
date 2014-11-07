class Point:
    def __init__(self, a=0, b=0):
        self.x = float(a)
        self.y = float(b)
    def __str__(self):
        return "%f|%f"%(self.x,self.y)

class Solution:
    # @param points, a list of Points
    # @return an integer
    x_slope = float('inf')
    dict_cache = dict()
   # def _sort_points(self,p1,p2):
   #   stP1 = str(p1)
   #   stP2 = str(p2)
   #   if stP1 > stP2: return "%s,%s"%(stP1,stP2)
   #   return "%s,%s"%(stP2,stP1)
    def _calc_slope(self,p1,p2):
   #     k = self._sort_points(p1,p2)
   #     if k in self.dict_cache:
   #         return self.dict_cache[k]

        deltax = p1.x - p2.x
        deltay = p1.y - p2.y
        slope = -float('inf')
        if deltax == 0 :
          slope = self.x_slope
        else:
            try:
              slope = (deltay)/deltax
            except ZeroDivisionError:
              print 'zero division:', deltax
        #self.dict_cache[k] = slope
        return slope
    def maxPoints(self, points):
        length = len(points)
        if length < 3: return length

        max_num = 0
        for i in range(0,length):
            dict_slope = dict()
            p1 = points[i]
            same_cnt = 1
            for j in range(0,length):
                if i==j:continue
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    same_cnt += 1
                    continue

                slope = self._calc_slope(p1,p2)
                dict_slope[slope] = dict_slope.get(slope,0) + 1

            #for point i, all slopes counts
            if not dict_slope: 
                if same_cnt > max_num: max_num = same_cnt
            else:
                vals = dict_slope.values()
                for val in vals:
                    if same_cnt + val > max_num:
                        max_num = same_cnt+val
        return max_num
