import os,sys
def main():
    #配置
    cwd = sys.path[0]   #当前目录，不带\
    surffix=""
	nameList=walk4files(cwd,surffix)
	print(nameList)

def walk4files(dir,suffix = ""):
    nameList=[] 
    for root, dirs, files in os.walk(dir):
        for name in files:
            if suffix == "":
                nameList.append(name)
            elif re.findall(suffix+"$", name, re.I):
                nameList.append(name)
            else:
                continue
    return nameList
	
if __name__=="__main__":
main()
