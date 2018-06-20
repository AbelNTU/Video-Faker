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


def encry(video_path, cover_path, transform_number, method = 0):
    out_name = video_path.split('/')[-1][:-4]+"_"+cover_path.split('/')[-1][:-4]
    count = 0
    
    
    origin_cap = cv2.VideoCapture(video_path)
    cover_cap = cv2.VideoCapture(cover_path)
    # fps = origin_cap.
    if method == 1:
        os.mkdir(out_name)
        count = 0
    elif method == 0:
        out = cv2.VideoWriter("../network/"+video_path.split('/')[-1][:-4]+"_encry.mp4",cv2.VideoWriter_fourcc(*'avc1'),30.0,(480,360))
        #out = cv2.VideoWriter("../mp4/"+out_name+"_encry1.avi",cv2.VideoWriter_fourcc('M','J','P','G'),20.0,(480,360))
    else:
        print( 'There is no method %d you want to use \n 0 : Just output a mp4 file \n 1 : Out a series of picture' %
             method)
        return -1

    while(origin_cap.isOpened()):
        origin_ret, origin_frame = origin_cap.read()
        cover_ret, cover_frame = cover_cap.read()
        if (cover_ret == False):
            cover_cap.release()
            cover_cap = cv2.VideoCapture(str(cover_path))
            cover_ret, cover_frame = cover_cap.read()
        origin_frame = resize(origin_frame,480,360)
        cover_frame = resize(cover_frame,480,360)
        blur = np.uint8(np.ceil(origin_frame / transform_number))
        blur = blur+np.uint8(np.ceil(cover_frame / 2))
        
        if(origin_ret == True):
            count+=1
            if method == 0:
                count = 0
                out.write(blur)
            elif method == 1 and count < 1000:
                cv2.imwrite("./"+out_name+"/%04d.jpg" % count, blur)
                count+=1
        else:
            break
        #cv2.imshow("blur",blur)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    count+=1
        #    break
        
    origin_cap.release()
    cover_cap.release()
    out.release()
    cv2.destroyAllWindows()