# x=list(range(1,5))
# print(x)

# type conversion list to string
# cool_list = ['H', 'e', 'l', 'l', 'o']
# cool_string = str.join('', cool_list)
# print(cool_string)

# reverse string
# mystrig = 'sonam'
# my_str = mystring[::-1]
# print(my_str)

# check datatype

# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

# for i in colors:
#     if isinstance(i,int):
#         print(i)

# iteration over functions
# def celsius_to_kelvin(cels):
#     return cels + 273.15
 
# for temperature in [9.1, 8.8, -270.15]:
#     print(celsius_to_kelvin(temperature))

# iteration over dictionary

# student_grades = {"sonam":70,"jamsok":80}

# for i in student_grades.values():
#     print(i)

# loop with string format

# student_grades = {"sonam jamtsho":70,"jamsok sonam":80}
# for key, Values  in student_grades.items():
#     print(f"{key}: +{Values}")

# for i in student_grades.items():
#     print(f"{i[0]} has got {i[1]} in math")

# replace + with 00 in values
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for i in phone_numbers.values():
#     print(i.replace('+', '00'))


# test your learning so far
# print('enter / to terminate the program')
# def sentance_maker(phrase):
#     question_tag=("how","why","what","when")
#     sentence=phrase.capitalize()
#     if phrase.startswith(question_tag):
#         return "{}?".format(sentence)
#     else:
#         return"{}.".format(sentence)
# # print(sentance_maker("what's your name"))

# results = []
# while True:
#     user_input=input('Say something:')
#     if user_input=="/":
#         break
#     else:
#         results.append(sentance_maker(user_input))

# print(" \n".join(results))

#  ................list comparation...............

# temperature = [220,230,233,234]

# new_temps = [temps/10 for temps in temperature]
# print(new_temps)

# temp = []
# for i in temperature:
#     temp.append(i/10)
# print(temp)

# show only int datatypes

# data = [99, 'no data',95, 94, 'no data']

# def foo(data):
#     return [i for i in data if isinstance(i,int)]
# print(foo([99, 'no data',95, 94, 'no data']))

# def foo(data):
#     return[i if not isinstance(i, str) else 0 for i in data]
# print(foo([99, 'no data',95, 94, 'no data']))

# simple question........
# def foo(a,b):
#     for i in a:
#         ns= sorted(a)
#     for j in b:
#         ans = sorted(b)
#     if(ns==ans):
#         return "anogram"
#     else:
#         return "not anogram"
# print(foo("tin","int"))


# palindorme
# def foo(a):
#     for i in a:
#         reversed_word= a[::-1]
#     if reversed_word == a:
#         return 'palindrome'
#     else:
#         return 'not a palindrome'
# print(foo('racecar'))

#  how to read txt files 
# enjoy = open("fruits.txt")
# print(enjoy.read())

# ........print multiple times..........
# content = enjoy.read()
# print(content)
# print(content)

# ................with method or with context manager to read file...............
# with open("fruits.txt") as file:
#     content = file.read()
# print(content)
# print(content)

#  ......writing and reading file...............

# with open("files/vegetable.txt", "w") as file:
#     file.write(" pumkin\n carrot\n saag\n")
#     file.write(" garlic")

# ......count words in the text........
# def foo(character,filepath="files/fruits.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(character)
# print(foo("apple"))


# ...........making shapes.........
#       *
#     * * *
#   * * * * *
# * * * * * * *

# shape = 4
# for i in range(0,shape):
#     for j in range(0,shape-i):
#         print('i', end="")
    # for k in range(0,2*i+1):
    #     print('*',end="")
    # print('*')

# num = 5
# for i in range(0,num):
#     for j in range(0,i+1):
#         print('*', end=' ')
#     print()

# ...........leetcode solutions.......
# ............Q1............ 
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]

# nums = [3,1,2,4]
# arr=[]
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         arr.append(nums[i])
# for j in range(len(nums)):
#     if nums[j]%2!=0:
#         arr.append(nums[j])
# print(arr)

# ...........Q2............
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# def check_sum_of_element(nums,target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j]==target:
#                 return [i,j]
# print(check_sum_of_element([2,7,11,15],18))

# .............Q3.............
# def isPalindrome(word):
#     if word[::-1]==word:
#         return True
#     else:
#         return False
# print(isPalindrome('racecar'))

# .............Q4.............
# num1='i'
# # num4='iv'
# num5='v'
# # 10=x

# def roman_number(num):
#     for i in range(num):
#         if num<4:
#             print(num1, end='')
#         elif num  5:
#             print(num5,end='')

# # print(roman_number(2))
# roman_number(3)

# ..............Q4................

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# count=0
# res=[]
# def Backspace_String_Compare(s):
#     for i in range(len(s)):
#         if i!='#':
#             res.append(s[i])
#         elif len(res)!=0:
#             res.pop(-1)
            
# print(Backspace_String_Compare(res['ab#']))

# def backspaceCompare(S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: bool
#         """
#         # if S == T:
#         #     return True
#         s_stack = []
#         t_stack = []
#         for c in S:
#             if c != '#':
#                 s_stack.append(c)
#             elif len(s_stack) != 0:
#                 s_stack.pop(-1)
#         for c in T:
#             if c != '#':
#                 t_stack.append(c)
#             elif len(t_stack) != 0:
#                 t_stack.pop(-1)
#         # return ''.join(s_stack) == ''.join(t_stack)
#         if s_stack==t_stack:
#             return True
#         else:
#             return False
# print(backspaceCompare('ab##','a#b#'))

# .............number pyramid...........
# number=int(input('enter any number:'))

# for i in range(number):
#     for j in range(i,-1,-2):
#         print(j,end=' ')
#     print('')

# ......................cap odd........................
# def cap_convert(word):
#    for i in range(len(word)):
#        if i%2==0:
#            temp=word[i]
#            print(temp.lower(),end='')
#        else:
#             print(word[i].upper(),end='')
# cap_convert('Anthropomorphism')
# ....................lesser_of_two_even.................
# def lesser_even(n,w):
#     if n%2==0 and w%2==0:
#         return min(n,w)
#     else:
#         return max(n,w)
# print(lesser_even(3,4))
# ......................animal cracker..............
# def animal_cracker(word):
#     temp = word.split(' ')
#     print(temp)
#     # temp[0][1]=temp[1][0]
#     return temp[0][0]==temp[1][0]
# print(animal_cracker('lamchoe ephent'))
# ......................makes twenty............
# def makes_twenty(n,m):
#     if n+m==20:
#         return True
#     elif n==20 or m==20:
#         return True
#     else:
#         return False
# print(makes_twenty(2,18))
# .......................old MacDonald..............

# def old_macdonald(word):
#     if len(word)>3:
#         return word[:3].capitalize()+word[3:].capitalize()
#     else:
#         return "word too short!"
# print(old_macdonald('sonam'))

# ...................master Yoda.........

# def reverse_word(word):
#     return ' '.join(word.split()[::-1])
# print(reverse_word('i love coding'))

# ...............almost there............

# def almost_there(num):
#     if num<100 and num>10:
#         if num%10<=10:
#             return True
#         else:
#             return False
#     elif num>=100 and num<200:
#         if num%100<=10:
#             return True
#         else:
#             return False 
#     elif num>=200 and num<300:
#         if num%200<=10:
#             return True
#         else:
#             return False
#     else:
#         return "sorry number out of bound"
# print(almost_there(30))
# def almost_there(n):
#     return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
# print(almost_there(90))

# ............. FIND 33...........
# def find_33(num):
#    for i in range(len(num)):
#        if i==3:
#            if num[i-1]==3 or num[i+1]==3:
#                return True
#        else:
#             return False
# print(find_33([3,3,2]))
