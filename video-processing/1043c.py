
# coding: utf-8

# # 1 把影片變白色 要可逆
# # 2 用照片覆蓋 然後再減掉照片還要可逆
# # 3 用影片覆蓋 可逆

# In[20]:


import cv2
import numpy as np
from PIL import Image
cover = cv2.imread("0003.jpg")
covered = cv2.imread("testchange.jpg")
if (cover[1] != covered[1]) or (cover[2] != covered[2])
    height = covered[1]
    width = covered[2]
    im = Image.open("0003.jpg")
    newcovered = im.resize((width,height),Image.BILINEAR)
    newcovered.save("testcover.jpg")


# In[14]:


import cv2
import numpy as np
cover = cv2.imread("0003.jpg")
covered = cv2.imread("testchange.jpg")
print(cover[1])


# In[6]:


from PIL import Image
im = Image.open("0003.jpg")
newcovered = im.resize((100,200),Image.BILINEAR)
newcovered.save("testchange.jpg")


# In[ ]:


coverimage = Image.open()
coveredimage = Image.open()
cover = cv2.imread()
covered = cv2.imread()
if cover[1] > covered[1]
    


# In[3]:


import os
os.sys.path


# In[18]:


import numpy as np
import cv2


# In[ ]:


## convert video to scale 640*480

vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0;
print "I am in success"
while success:
  success,image = vidcap.read()
  resize = cv2.resize(image, (640, 480)) 
  cv2.imwrite("%03d.jpg" % count, resize)     
  if cv2.waitKey(10) == 27:                     
      break
  count += 1


# In[19]:


cap = cv2.VideoCapture('video.mp4')

def make_480p():
    cap.set(3, 360)
    cap.set(4, 480)
make_480p()
while(cap.isOpened()):
    ret, frame = cap.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(gray)
    #print(type(gray[0][0]))
    #print(gray.max())
    gray_n = np.ceil( gray / 20 )
    gray_n = np.uint8(gray_n)
    #print(gray_n.max())
    #print(gray_n.shape)
    gray_n = gray_n
    #white = np.full(shape=(480,873),dtype=np.uint8,)
    #print(type(gray_n[0][0]))
    cv2.imshow('frame',gray_n)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

