import os,sys

def main():
	cwd = sys.path[0]
	nameList = []
	nameList = walk4files(cwd,"")
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
