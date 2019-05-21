
# coding=utf-8    
from PIL import Image  
import os
import json 
  
def mkdir(path):  
   
    # 去除首位空格  
    path=path.strip()  
    # 去除尾部 \ 符号  
    path=path.rstrip("\\")  
   
    # 判断路径是否存在  
    # 存在     True  
    # 不存在   False  
    isExists=os.path.exists(path)  
   
    # 判断结果  
    if not isExists:  
        # 如果不存在则创建目录  
        print (path+' 创建成功')  
        # 创建目录操作函数  
        os.makedirs(path)  
        return True  
    else:  
        # 如果目录存在则不创建，并提示目录已存在  
        return False  

  

name = 'game'
imageName = name + '.png'  
img = Image.open(imageName)
mkdir(name) 

with open(name+'.json','r',encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    frames=load_dict['frames']
    for key in frames:
        vertices=frames[key]
        fileName ='%s/%s.png' %(name, key)
        print(fileName,vertices)
        X = vertices['x'] 
        Y = vertices['y'] 
        X_end = vertices['x'] + vertices['w']
        Y_end = vertices['y'] + vertices['h']
        img.crop((X, Y, X_end, Y_end)).save(fileName)  
