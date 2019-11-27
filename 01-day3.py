# 比較一下範例檔案中的「File I/O」與「xmltodict」讀出來的內容有什麼差異
# 根據範例檔案的結果：
# 1. 請問高雄市有多少地區有溫度資料？
# 2. 請取出每一個地區所記錄的第一個時間點跟溫度
# 3. 請取出第一個地區所記錄的每一個時間點跟溫度
forder_path="Data"


#使用xml.dom
print("\n####\n使用xml.dom")
import xml.dom.minidom 
# 存取檔案
doc = xml.dom.minidom.parse(forder_path+"/sample.xml")
# 存取我們的資訊
print(doc.getElementsByTagName("Title")[0].firstChild.nodeValue)
# 用迴圈存取我們的資訊
chapters = doc.getElementsByTagName("Chapter")
for chapter in chapters:
    print (chapter.getAttribute('name'), chapter.firstChild.nodeValue)


#使用xml.etree
print("\n####\n使用xml.etree")
import xml.etree.ElementTree as ET  
tree = ET.parse(forder_path+"/sample.xml") 
root=tree.getroot()
# print(root)
root_title =root[0].text
print(root_title)
root_Chapters =root[2]
for row in root_Chapters:
    pass
    #print(row.attrib["name"],row.text)

import xmltodict
# 存取檔案
with open(forder_path+"/64_72hr_CH.xml", encoding = 'utf8') as fd:
    doc = dict(xmltodict.parse(fd.read()))

# 1. 請問高雄市有多少地區有溫度資料？
chapters = doc['cwbopendata']['dataset']['locations']['location']

count = sum(1 for x in chapters)
print("請問高雄市有多少地區有溫度資料？", count)

# 2. 請取出每一個地區所記錄的第一個時間點跟溫度
i=0
while i<=37:

    locationName_list = doc['cwbopendata']['dataset']['locations']['location'][i]['locationName']#地區   
    location_dataTime = doc['cwbopendata']['dataset']['locations']['location'][i]['weatherElement'][0]['time'][0]['dataTime']#第一個時間點  
    location_weather_measures= doc['cwbopendata']['dataset']['locations']['location'][i]['weatherElement'][0]['time'][0]["elementValue"]["measures"]#第一個時間點的溫度
    location_weather_= doc['cwbopendata']['dataset']['locations']['location'][i]['weatherElement'][0]['time'][0]["elementValue"]["value"]#第一個時間點的溫度
    
    print(locationName_list,location_dataTime,location_weather_measures,location_weather_)#第一個時間點
    i+=1

# 3. 請取出第一個地區所記錄的每一個時間點跟溫度
print("\n####\n")
first_location = doc['cwbopendata']['dataset']['locations']['location'][0]['locationName']
                      
print(first_location)
first_location_rows = doc['cwbopendata']['dataset']['locations']['location'][0]['weatherElement'][0]['time']
for list_ in first_location_rows:
    dataTime_=list_["dataTime"]
    measures_=list_["elementValue"]["measures"]
    weather_=list_["elementValue"]["value"]
    print(dataTime_,measures_,weather_)