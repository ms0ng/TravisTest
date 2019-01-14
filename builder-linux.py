#-*- coding: utf-8 -*-
#encoding=utf-8
#coding:utf-8
import os,re,subprocess,sys



def main():
    #配置
    cwd = sys.path[0]   #当前目录，不带\
    retry=5
    surffix="c"

    dirList=walk4dirs(cwd,"实验.+",re.M)
    for name in dirList:
        wdir=cwd+"\\"+name
        buildPic(wdir,retry,"c")

#参数 ： 工作目录(不带\),重试次数,文件后缀过滤
def buildPic(wdir,retry=5,surffix=""):
    fileList=walk4files(wdir,"c")
    fileList_noSpace=sort(fileList)
    failedPic=[]
    cmdOut=[]
    #开始工作
    run("mkdir "+wdir+"\\pic")
    for i in range(len(fileList)):
        print("第"+str(i)+"个文件，共"+str(len(fileList))+"个")
        if os.path.isfile(wdir+"\\pic\\"+fileList_noSpace[i]+".png"):
            print(fileList[i]+"的图片已存在\n")
            continue
        for j in range(retry+1):
            print("生成"+fileList_noSpace[i]+".png中\n")
            msg = run(genCMD(wdir+"\\"+fileList[i],fileList_noSpace[i],wdir))
            if os.path.isfile(wdir+"\\pic\\"+fileList_noSpace[i]+".png"):
                print(fileList[i]+"-----------------------生成成功("+str(j)+"次重试)\n")
                break
            if(j==(retry+1)):
                print(fileList[i]+"生成失败\n")
                failedPic.append(fileList[i])
        cmdOut.append(msg)
        #-----------------------------------------------------------------

    #生成README.md
    print("开始生成README")
    with open(wdir+"\\README.md",'w',encoding="utf-8") as f:
        wdirname = wdir.split("\\")[-1]     #当前目录名
        f.write("# 金陵科技学院-18数字媒体技术-"+wdirname+"\n")
        f.write("> 此文档及相关图片由程序自动生成\n")
        for i in range(len(failedPic)):
            f.write("\t"+failedPic[i]+" 的图片生成失败\n")
        f.write("\n")
        f.write("在上面的文件列表中点击相关文件名即可阅览/复制源代码\n")
        f.write("以下为图片阅览\n")
        for i in range(len(fileList)):
            f.write("### "+fileList[i]+"\n")
            f.write("!["+fileList[i]+"](./pic/"+fileList_noSpace[i]+".png)\n")
    print("README文档生成成功")



#根据参数输出生成图片的命令，返回一个字符串
#文件名，欲生成的图片名(不需带后缀，默认.png),生成图片文件夹(不需加\，会自动生成在该文件夹下的pic里面)
def genCMD(generatedFile,targetName,outputDir):
    cmdstr="carbon-now \""+generatedFile+"\" -t "+targetName+" -l "+outputDir+"\pic -h"
    return cmdstr

#执行CMD命令，返回字符串结果，这是一个堵塞方法
def run(cmds):
    try:
        sub=subprocess.check_output(cmds,shell=True)
        return str(sub.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        return str(e.output)
       

#处理一个List，为每一个output去空格
def sort(alist):
    newlist=[]
    for i in alist:
        newlist.append(re.sub(' ','',i))
    return newlist

#遍历某个目录的所有文件(可以指定后缀名,例"c",不包括点)，返回一个List
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

#正则遍历某个目录的所有文件夹，返回一个List.若正则为空，则遍历所有文件夹
def walk4dirs(dir,reg="",tag=re.I):
    dirList=[]
    for root, dirs, files in os.walk(dir):
        for name in dirs:
            if reg == "":
                dirList.append(name)
            elif re.findall(reg, name,tag):
                dirList.append(name)
            else:
                continue
    return dirList

if __name__=="__main__":
    main()
