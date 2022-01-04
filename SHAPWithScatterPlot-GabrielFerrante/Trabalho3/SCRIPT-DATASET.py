#!/usr/bin/env python
# coding: utf-8

# In[4]:

#Execute o comando para baixar as annotations das imagens do DATASET COCO, é necessário para realizar o donwload das imagens

#!wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip

#INSTALE A API DO COCO DATASET - pip install pycocotools (N EXISTE PARA WINDOWS)
from pycocotools.coco import COCO
import requests


# In[5]:


#SCRIPT PARA BAIXAR O DATASET DE IMAGENS PARA UTILIZAR A FUNÇÃO DO XAI COM O SHAP
def createDirectory(name, animal):
    import os
 
    path = name
    access_rights = 0o755
    try:
        os.mkdir(path, access_rights)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        
    else:
        print ("Successfully created the directory %s " % path)


def downloadValid(animal, coco, index):
    createDirectory('valid/', animal)
    cats = coco.loadCats(coco.getCatIds())
    nms=[cat['name'] for cat in cats]

    catIds = coco.getCatIds(catNms=[animal])

    imgIds = coco.getImgIds(catIds=catIds )
    images = coco.loadImgs(imgIds)

    i = 1
    for im in images:
        if i <= 50:
            img_data = requests.get(im['coco_url']).content
            
            with open('valid/'+ animal+'_'+im['file_name'], 'wb') as handler:
                handler.write(img_data)
            
            #time.sleep(3)    
            i = i + 1
        else:
            break


# In[6]:


coco = COCO('annotations/instances_val2017.json')
animals = [ 'bird',
            'cat',
            'dog',
            'horse',
            'sheep',
            'cow',
            'elephant',
            'bear',
            'zebra',
            'giraffe']
for item in animals:
  downloadValid(item, coco, animals.index(item))

