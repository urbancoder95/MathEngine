import os
def assign_name():
    if(not os.path.exists("temp_names.txt")):
        f = open('temp_names.txt', 'w+')
        f.write(str(1))
        f.close()
        return "X1"
    else:
        f = open('temp_names.txt', 'r')
        s = f.read()
        s = s.split('\n')
        s = [int(x) for x in s]
        i = 1
        while(i in s):
            i += 1
        f.close()
        f = open('temp_names.txt', 'a')
        f.write(str(i))
        f.close()
        return "X"+str(i)
