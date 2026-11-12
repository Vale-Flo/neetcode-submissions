class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:    
            if i == '+':
                record += [record[-1]+record[-2]]
                # print(record)
            
            elif i == 'C':
                record = record[:-1]
                # print(record)

            elif i == 'D':
                record += [2* record[-1]]
                # print(record)
            
            else:
                record += [int(i)]
                # print(record)

        # suma = 0
        # for i in record:
        #     suma += i
        # return suma
        return sum(record)
