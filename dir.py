'''

1. Shell directory navigation logging (specific title can not remember）
Give a List<String> moves, each string represents a shell navigation command.
There are three types of command given：
"./ "Indicates to stay in the current directory
"../ "Indicates return to parent directory
"x /" means to enter a X subdirectory
Question: how many layers (an int) are required to return to the
main directory when these moves are executed from the main directory?
Note that the main directory does not have parent directory, so do it on main"../ "Is invalid.
Example: ["a/","./ ", "b/",".."/ " ,".."/ " ,"../ ", "c/"]
the layer corresponding to each step is /a -> /A -> /b - > /a - > / - > / - > / - > / c,
so finally you need 1 step to return main from /c and the answer is 1.

'''
ls= ["a/","!", "b/","..!","..!","..!" ,"c/"]
stk=[]

for i in ls:
    if i=="!":
        continue
    elif i == "..!":
        if len(stk)>0:
            stk.pop()
    else:
        stk.append(i)


print(stk)
print(len(stk))