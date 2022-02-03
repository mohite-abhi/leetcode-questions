from collections import Counter
import enum

# approach 1
def intToRoman(num):
    valid = True
    minus = False
    roman = [
        ['I', 1, 0, 0],
        ['V', 5, 0, 0],
        ['X', 10, 0, 0],
        ['L', 50, 0, 0],
        ['C', 100, 0, 0],
        ['D', 500, 0, 0],
        ['M', 1000, 0, 0]
    ]

    def makeValid(roman, minus):
        if minus:
            return
        for i in range(len(roman)):
            limit = 1 if i%2 else 3
            if minus:
                limit = 1 if i%2 else 4

            if roman[i][2] > limit:
                if i%2:
                    roman[i][3] = 0 
                else:
                    roman[i][3] = -1
                minus = True
                roman[i][2] = 0
                roman[i+1][2] += 1


    def romanizeCode(roman):
        code = ['']*100
        i = 0
        j = 0
        while i < len(roman):
            if code[j] != '':
                j += 1
                continue
            
            if roman[i][2] > 0:
                code[j] = roman[i][0]
                roman[i][2] -= 1
                
            elif roman[i][3] == -1:
                code[j+1] = roman[i][0]
                roman[i][3] = 0
                continue
                
            if roman[i][2] == 0 and roman[i][3] == 0:
                i += 1
                continue
            
        
        return "".join(code[::-1])



    i = len(roman) - 1
    while num != 0 or valid == False:
        if valid == False:
            makeValid(roman, minus)
            valid = True

        if num < roman[i][1]:
            i -= 1
            continue
        
        limit = 1 if i%2 else 3
        roman[i][2] += num // roman[i][1]
        num %= roman[i][1]
        if roman[i][2] > limit:
            valid = False

        i -= 1
        print(roman)

    
    return romanizeCode(roman)
    

# approach 2
def intToRoman(num):
    coding = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD' : 400,
        'C' : 100,
        'XC' : 90,
        'L' : 50,
        'XL' : 40,
        'X' : 10,
        'IX' : 9,
        'V' : 5,
        'IV' : 4,
        'I' : 1
        }

    roman = []
    for i in coding:
        if num >= coding[i]:
            multiple = num // coding[i];
            num %= coding[i];
            roman.append(multiple*i)

    return "".join(roman)



