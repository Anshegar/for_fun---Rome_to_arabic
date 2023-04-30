'''
Task:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''



class Solution():
    def __init__(self, roman):
        self.roman = roman.upper()
        self.roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def approve(self):

        # Check to make sure there are no four I's in a row after the char
        for i in range(len(self.roman) - 3):
            if self.roman[i] == 'I' and self.roman[i + 1] == 'I' and self.roman[i + 2] == 'I' and self.roman[i + 3] == 'I':
                return 'Not approved'
        # Check that there is no more than 1 I before char and that char exists and is not equal to i  
        for i in range(len(self.roman) - 2):
            if self.roman[i] == 'I' and self.roman[i + 1] == 'I' and self.roman[i + 2] != None and self.roman[i + 2] != 'I' :
               return 'Not approved'
        
        return 'approved'

    def roman_to_arabic(self):

        keys_list = list(self.roman_map.keys())
        keys_list
        values_list = list(self.roman_map.values())
        values_list
        char_list= []
        char_dic = {}
        char_dic_result = {}
        prev = 0
        result = []


        # Identify multisystem chars, the smalest in front, the oldest in second. We make the smalest negative to calculate the result 
        # and get the value of these two digits. Making list of this results (we can revers list but its not necessary)
        for i in range(len(self.roman)-1, -1, -1):
            curr = self.roman_map[self.roman[i]]
            if curr < prev:
                result.append(-curr)
            else:
                result.append(curr)
            prev = curr
        result

        # Loop, find len of result list. Search negative numbers in it and nub after. (5, -1). Find the sum of the numbers (corresponding to the Roman signs)
        # Looking for keys in the dictionary that correspond to the found values of the numbers (V, I)
        # Create a dictionary to compare Roman and Arabic characters present in the original number
        for i in range(len(result)):
            if result[i]<0:
                result_sum = result[i-1] + result[i]
                a=''
                b=''
                for ii in range(len(values_list)):
                    if values_list[ii] == - result[i]:
                        a=keys_list[ii]
                for iii in range(len(values_list)):
                    if values_list[iii] == result[i-1]:
                        b=keys_list[iii]

                total_key = a+b
                
                char_dic[total_key] = result_sum

            # Выявляем все многосоставные числа( они состоят из положительного и отрицательного числа идущих подряд) 
            # и оставшиеся числа заносим в словарь присваивая им соответствующий ключ из словаря романских чисел
            # We find all the composite numbers (they consist of positive and negative numbers in a row) 
            # and put the remaining numbers in the dictionary by assigning them to the appropriate key from the dictionary of Romanesque numbers
            else:
                for k,v in self.roman_map.items():
                    # Поиск римского целого римского числа(оно всегда положительное арабское) с перехватом ошибок, так как в конце может 
                    # быть целое число, а не составное и его тоже надо будет вписать
                    # Search for a Roman integer roman number (it is always a positive arabic number) with error-catching, because it may 
                    # be a whole number instead of a composite number and you will also have to write
                    try:
                        if int(v) == result[i]  and result[i+1]>0:
                            if self.roman_map[k] == result[i]:
                                # Check for repeat of characters in a row, to identify the "I" set
                                if k in char_dic:
                                    char_dic[k] = char_dic[k] +1
                                    pass
                                else: 
                                    char_dic[k] = result[i]

                            pass


                    except Exception as e:
                        # Проверка совпадает ли ключ и value со словарем римских цифр, так как из-за цикла он будет кидать к значению 
                        # все подряд ключи, а мы отсеем неверные
                        # Check if key and value match the dictionary of roman numerals, because it will throw to value 
                        # all the keys in a row, and we will weed out the wrong ones
                        if self.roman_map[k] == result[i]:
                            if k in char_dic:
                                char_dic[k] = char_dic[k] +1
                                pass
                            else: 
                                char_dic[k] = result[i]

        # To make it easier to read, we first turn the dictionary (probably should have flipped one of the key lists at the beginning :) )
        keys_list_char_dic = list(char_dic.keys())
        keys_list_char_dic.reverse()
        values_list_char_dic = list(char_dic.values())
        values_list_char_dic.reverse()
        values_list.reverse()
        for char in range(len(keys_list_char_dic)):
            char_dic_result[keys_list_char_dic[char]] = values_list_char_dic[char]

        if self.approve() == 'Not approved':
            return 'There is no such number: {0}'.format(self.roman)
        else:
            arabic = 0
            prev_value = None

            for char in self.roman:
                value = self.roman_map[char]
                char_list.append('{0} = {1}'.format(char,value))
                

                if prev_value is not None and prev_value < value:
                    arabic = arabic - prev_value
                    value = value - prev_value

                arabic = arabic + value
                prev_value = value
            
            if 1 <= int(arabic) <= 3999:       
                # char_dic_result char_list
                return 'Input: s = {0} \nOutput: {1} \nExplanation: {2}.'.format(self.roman, arabic, char_dic_result)
            else:
                return 'Out of range "s"'


s = 'MCMXCIV'
if  1 <= len(s) <= 15:
    rta = Solution(s)
    arabic = rta.roman_to_arabic()
    print(arabic)
else:
    print('to long input')


