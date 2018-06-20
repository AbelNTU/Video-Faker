import os
from PIL import Image
import numpy as np
import cv2


def resize(image,width,height):
    try:
        im = Image.fromarray(image)
        new = im.resize((width,height),Image.BILINEAR)
        return np.array(new)
    except:
        return 0

def decry(video_path, cover_path,transform_number):
    out_name = video_path.split('/')[-1][:-4]+"_"+cover_path.split('/')[-1][:-4]
    #out = cv2.VideoWriter(out_name+"_decry.avi",cv2.VideoWriter_fourcc('M','J','P','G'),20.0,(480,360))
    #out = cv2.VideoWriter("../mp4/"+out_name+"_decry.mp4",cv2.VideoWriter_fourcc(*'mp4v'),25.0,(480,360))
    origin_cap = cv2.VideoCapture(video_path)
    cover_cap = cv2.VideoCapture(cover_path)
    while(origin_cap.isOpened()):
        origin_ret, origin_frame = origin_cap.read()
        cover_ret, cover_frame = cover_cap.read()
        if (cover_ret == False):
            cover_cap.release()
            cover_cap = cv2.VideoCapture(str(cover_path))
            cover_ret, cover_frame = cover_cap.read()
        #origin_frame = resize(origin_frame,480,360)
        cover_frame = resize(cover_frame,480,360)
        blur = origin_frame - np.uint8(np.ceil(cover_frame / 2))
        blur*=transform_number
        if(origin_ret == True):
            pass
            #out.write(blur)
        else:
            break
        cv2.imshow("blur",blur)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
        
    origin_cap.release()
    cover_cap.release()
    out.release()
    cv2.destroyAllWindows()