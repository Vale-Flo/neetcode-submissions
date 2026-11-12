class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals is initially sorted in ascending order by start_i
        
        # intervals += [newInterval]
        # intervals.sort()
        # interv_2 = []

        # if len(interv_2) == 0:
        #     return []
        
        # interv_2 += [[intervals[0][0], intervals[0][1]]]
        
        res = []
        start_new = newInterval[0]
        end_new = newInterval[1]

        for i in range(len(intervals)):
            start_int = intervals[i][0]
            end_int = intervals[i][1]

            if end_int < start_new:
                res += [[start_int, end_int]]
            
            elif start_int > end_new:
                res += [[start_new, end_new]]
                return res + intervals[i:]

            else:
                start_new = min(start_new, start_int)
                end_new = max(end_new, end_int)
        
        res += [[start_new, end_new]]

        return res               