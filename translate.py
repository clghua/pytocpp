tabNum = 0 #This number indicates the number of tabs used for the program

def mergeAndTranslate(a1, a2, a3):
    return translate(a1 + a2 + a3)

''' using the list of formatted output, translates python into c++ '''
def translate(a1):
    global tabNum
    #From the beginning of the list, join them into a string
    c = ""
    for i in range(len(a1)):
        if(type(a1[i]).__name__ == "str"): #Adding strings... obviously
            c += a1[i]
            #Checking for body checks
            if '{' in a1[i] or '}' in a1[i] or ';' in a1[i]: #Checking for end line to add tabs
                if '{' in a1[i]:
                    c += "\n"
                    tabNum += 1
                elif '}' in a1[i]:
                    #if tabNum > 0:
                        #c = c[:-2] + c[-1] #Deleting second last character in string (which should be a tab)
                    c += "\n"
                    tabNum -= 1
                for i in range(tabNum):
                    c += "\t"
        elif type(a1[i]).__name__ == "float" or type(a1[i]).__name__ == "int": #Joining numbers
            c += str(a1[i])
        elif type(a1[i]).__name__ == "list": #Recursive call on a list
            c += translate(a1[i])

    return c

#This is an example, please change accordingly
a = ["#include <iostream>\n", "using namespace std;\n"]
b = []
c = ["int main () {", "int a", ";\n", "a", " = ", [2, " * ", 5.6], " + ", 4, ";\n","return 0;\n" + "}"]
print (mergeAndTranslate(a, b, c))