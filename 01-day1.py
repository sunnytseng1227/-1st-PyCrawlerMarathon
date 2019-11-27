#D1：資料來源與檔案存取
# 1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
# 2.（實作）完成一個程式，需滿足下列需求：
# 「下載指定檔案到 Data 資料夾，存成檔名 Homework.txt」的檔案網址：https://www.w3.org/TR/PNG/iso_8859-1.txt 或任一個 .txt 的檔案網址
# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
# 將「Hello World」字串覆寫到 Homework.txt 檔案
# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

#--------------------------------------------------
#自已的想法：
#一. 要 import 能使用url的lib，把已知的目標檔案存到指定資料夾
# 1.1 已知的檔案名稱作法
# 1.2 已知的副檔名作法
# 1.3 如何在不知道有沒有指定資料夾的情況下將檔案安全儲存
# 1.4 如果目標檔案不存在，應該報錯或不執行

#二、檢查下載的檔案是否真的存在指定資料夾，且檔名正確
#三、寫入一串文字於下載後的檔案
#四、取得檔案內文字為變數A，並檢查變數A是否符合寫入的文字字串數

import urllib.request as req
#1.在過程中發現有二種方法
# 1、urlopen()：比較像是建立與物建的連線，並像讀檔案一般
# 2、urlretrieve：直接將遠端資料下載到本地
TargetPath = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
SaveFile="Homework.txt"
SaveFilePath ="./Data"
#1.3如何在不知道有沒有指定資料夾的情況下將檔案安全儲存
import os
# #1.4如果目標檔案不存在，應該報錯或不執行
import urllib.error as urlerror

try:
    req.urlopen(TargetPath)
    #print(os.path.isdir(SaveFilePath))
    if not os.path.isdir(SaveFilePath):
        os.mkdir(SaveFilePath)
    req.urlretrieve(TargetPath,SaveFilePath+"/"+SaveFile)
    #檢查檔案是否存在
    if os.path.isfile(SaveFilePath+"/"+SaveFile):        
        print("\n####\n檔案已下載至"+SaveFilePath)
        print("另存檔名為："+SaveFile)
        print(SaveFile+"檔案大小為：",os.path.getsize(SaveFilePath+"/"+SaveFile),"\n########")
        CopyWord="Hello World"
        CopyWord_Len=len(CopyWord)
        
        print("開始將字數長度為",CopyWord_Len,"的'"+CopyWord+"'的字串覆寫至檔案中")
        file=open(SaveFilePath+"/"+SaveFile,mode="w",encoding="utf-8") #寫入檔案
        file.write(CopyWord) #寫入字串        
        file.close() #關閉
        print("覆寫後的"+SaveFile+"檔案大小為：",os.path.getsize(SaveFilePath+"/"+SaveFile))

        GetWord_len=0        
        file=open(SaveFilePath+"/"+SaveFile,mode="r",encoding="utf-8") #讀取檔案
        GetWord_len = len(file.read())
        file.close() #關閉       
        print("覆寫後的"+SaveFile+"字數長度為：",GetWord_len)
       
       
       
    
except urlerror.HTTPError  as e:
    print("\n####"+e.reason+"\n"+TargetPath+"  "+e.reason+"\n########")
