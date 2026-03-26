# print("hey")
# user_Input=input("Enter Your Name")
# if(user_Input):
#     print("hello",user_Input)
# else:
#     print("Enter Something")
'''

Intial code Done!

'''

print("hello\"") #to put " this you have to use \ before
print("heyy\'") #to put ' this you have to use \ before
print("hello\\") #to put " this you have to use \ before
print("heyy\n") #Change the line
print("heyy\t hehehhe") #to put space after the word to \t

print("""
This is a multi-line string.
\tIt preserves line breaks 
\tand spacing.
""")

'''Enumerate()'''

a = ["Laiba","sadia","jazia","sabika"]
print(list(enumerate(a)),"\ndisplaying all of these in list")

aforloop= ["23","33","65"]

for i,v in enumerate(aforloop):
    print(i,v) #enumerate(a) returns pairs of (index, value), which are unpacked into i and v.


'''for index change follow the syntax enumerate(iteratable item,index)'''

for i,v in enumerate(aforloop,2):
    print(i,v)
    
# if loop isn't used then next() is there

print(next(enumerate(aforloop)))
# stored in variable 
e=enumerate(aforloop,1)
print("---")
print(next(e))#0 index
print(next(e))#1 index

'''dictionary with enumerate'''

dictionary_var = {"first":2,"Second":9,"Third":7}

for i,(k,v) in enumerate(dictionary_var.items()):
    print("Index is ",i,"key = ",k,"and here is the value ",v)