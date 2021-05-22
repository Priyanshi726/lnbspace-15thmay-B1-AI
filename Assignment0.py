#Ques 1.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
     ]
for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)

#Ques 2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))

#Ques 3.
import string
  
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")


#Ques 4.
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

#Ques 5.
print('\n---Q5 (generate the corresponding two integer list) ---\n')
input_string = input('Enter the string in required fashion : ')
input_list = input_string.split('#')
list_1 = input_list[0].split()
list_2 = input_list[1].split()
list_1 = [int(i) for i in list_1]
list_2 = [int(i) for i in list_2]

print('list 1 : ',list_1)
print('list 2 : ',list_2)

#Ques 6.
items = input("Input comma separated sequence of words: ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#Ques 7.
print('\n---Q7 (student with max marks) ---\n')
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],
     'Marks': [57,87,67,79]}

marks_list = d['Marks']
max_marks = max(marks_list)
max_marks_index = marks_list.index(max_marks)

student_list = d['Student']
print('Student with maximum marks : ',student_list[max_marks_index])

#Ques 8.
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

#Ques 9.
print('\n---Q9 (creates a new dictionary of students) ---\n')

d = {'Name': ['Akash', 'Soniy', 'Vishakha','Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

newData = {'Name' : [],'Ratings' : []}
index = 0
for sub in d['Subject']:
    if(sub == 'Python'):
        newData['Name'].append(d['Name'][index])
        newData['Ratings'].append(d['Ratings'][index])
    index += 1 

print('new dictionary of students : ',newData)

#Ques 10.
n = int(input())
divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print(divBy7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

divChecker(n)

#Ques 11.
pos=0
moves={"UP":1j,
       "DOWN":-1j,
       "LEFT":-1,
       "RIGHT":1}

#Set inputs
data=["UP 5",
    "DOWN 3",
    "LEFT 3",
    "RIGHT 2"]

#Move robot on valid moves
for inp in data:
    parts=inp.split()    
    mv=parts[0]
    val=parts[1]
    print (mv, val)
    pos += moves[mv]*int(val)

#get distance     
print('rounded distance from zero position:', round(abs(pos)))
