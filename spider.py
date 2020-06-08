import urllib.request
import urllib.parse
import lxml
from bs4 import BeautifulSoup
import time

nameList=[]
linkList=[]
relationList=[]
N=0

def spider():
    global N
    values = {'name': 'Zip','word': 'Hello'}
    data=bytes(urllib.parse.urlencode(values),encoding='utf-8')
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    request=urllib.request.Request(url=linkList[N][1],data=data,headers=headers,method='POST')
    response = urllib.request.urlopen(request)

    soup=BeautifulSoup(response.read(),'lxml')
    data=soup.select(rule)#喜欢这部电影/剧集的人也喜欢

    for item in data:
        if(item.img['alt'] not in nameList):
            nameList.append(item.img['alt'])
            linkList.append([item.img['alt'],item.get('href')])
        relationList.append([nameList[N],item.img['alt']])
      
    response.close()
    print(nameList[N]+'finish')
    print(len(nameList))
    N+=1

def buildArray():
    n=len(nameList)
    relationArray=[[0 for j in range(n)] for i in range(n)]
    for i in range(len(relationList)):
        relationArray[nameList.index(relationList[i][0])][nameList.index(relationList[i][1])]=1
    for i in range(n):
        print(relationArray[i])
    
if __name__=='__main__':
    url='https://movie.douban.com/subject/3319755/?from=subject-page'#怦然心动
    name='怦然心动'
    rule='#recommendations > div > dl > dt > a'
    nameList.append(name)
    linkList.append([name,url])
    
    start=time.time()
    while N<len(nameList) and N<10:
        spider()
        time.sleep(2)
        
    file1=open('nameList.txt','w',encoding='utf-8')
    file1.write(str(nameList))
    file1.close()

    file2=open('linkList.txt','w',encoding='utf-8')
    file2.write(str(linkList))
    file2.close()

    file3=open('relationList.txt','w',encoding='utf-8')
    file3.write(str(relationList))
    file3.close()

    buildArray()

    end=time.time()
    print('time used:',end-start)
    print('finished')
