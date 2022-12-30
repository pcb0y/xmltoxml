import glob
import xmltodict #导入 xmltodict
from xml.dom.minidom import Document
from lxml import etree
import datetime
import re
material={}
materials=[]
# xmlpath='./asset/xml'+'/尤加利多层板_9.xml'
for xmlPath in glob.glob("../xml" + "/*.xml"):
    # print(xmlPath)
    #解析XML文件
    with open(xmlPath,encoding='utf-8') as xmlfile:

    # tree=etree.parse(xmlpath)
        a=xmlfile.read()
        m=re.sub('panel\d+','panel',a)
        # f=re.sub('no.\d+','no',m)
        # g=re.sub('<no.*>','',f)
        # h=re.sub('</no>','',g)
        # print(h)
        xml=etree.XML(m)
        MaterialName=xml.xpath('//project/panel/@material')
        Width=xml.xpath('//project/panel/@l')
        Height=xml.xpath('//project/panel/@w')
        Quantity=xml.xpath('//project/panel/@num')
        Thickness=xml.xpath('//project/panel/@thickness')
        Quantity=len(Quantity)
        # for i in range(0,len(Quantity)):
        #     Width[i]='1220'
        #     Height[i] = '2440'
        material['MaterialName'] =MaterialName[0]
        material['Width']='1220'
        material['Height']='2440'
        material['Quantity']=str(Quantity)
        material['Thickness']=Thickness[0]
        materials.append(material)
        material={}
# print(materials)



#生成XML文件
doc = Document()
CutTask = doc.createElement("CutTask")
doc.appendChild(CutTask)
CutTask.setAttribute('Batch','20222222')
date = datetime.datetime.now()
CutTask.setAttribute('Date',str(date))
CutTask.setAttribute('Case','NC')
CutTask.setAttribute('App',' 1.0.6')
for len in materials:
    # print(len)
    Material=doc.createElement('Material')
    CutTask.appendChild(Material)
    MaterialName=materials[0].get('MaterialName')
    Material.setAttribute('MaterialName',len.get('MaterialName'))
    Thickness=materials[0].get('Thickness')
    Material.setAttribute('Thickness',len.get('Thickness'))
    Boards=doc.createElement('Boards')
    Material.appendChild(Boards)
    B=doc.createElement('B')
    Boards.appendChild(B)
    Boards.setAttribute('UsedArea','1')
    Boards.setAttribute('Percent','1')
    Boards.setAttribute('UsedQuantity', '1')
    Width=materials[0].get('Width')
    B.setAttribute('Width',Width)
    Height=materials[0].get('Height')
    B.setAttribute('Height',len.get('Height'))
    Quantity=materials[0].get('Quantity')
    B.setAttribute('Quantity',len.get('Quantity'))
filename=str(date)
filename=re.sub('\D+','',filename)

filename ='../xin/'+filename+'.xml'
print(filename)
f = open(filename, "w",encoding='utf-8')
f.write(doc.toprettyxml(indent=" "))
f.close()