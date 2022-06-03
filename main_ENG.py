import os
import sys
import numpy as np
from PIL import Image, ImageDraw
import cv2
import matplotlib.pyplot as plt
import re
import glob
import time

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

if __name__ == "__main__":
    # Check ID
    args = sys.argv
    try:
        qid = int(args[1])
    except:
        print("Please input your subquestions2 ID.")
        exit()

    max_id = 17
    if (qid < 0) or (qid > max_id):
        print("ID must be 1 - %d"%(max_id))
        exit()

    # Define path and file
    img_dir = 'imgs'
    res_name = 'result_'+str(qid)+'.txt'

    with open(res_name, 'w') as f:
        f.write(str(qid) + '\n')

    # Get image files
    imgfiles = sorted(glob.glob(img_dir + "/*"), key=natural_keys)

    # debug
    with open("imgfiles.txt", 'w') as f:
        for imgfile in imgfiles:
            f.write(imgfile + '\n')

    fig = plt.figure()

    # evaluation all images    
    for count, imgfile in enumerate(imgfiles):
        imgname = imgfile.split("/")[-1]
        if os.path.exists(os.path.join(img_dir, imgname)):
            gray = cv2.imread(os.path.join(img_dir, imgname),cv2.IMREAD_GRAYSCALE)

            # 画像サイズ取得
            H,W = gray.shape
            
            # 画像合成（背景真っ黒の画像の上に画像貼り付け）
            H_back = 128
            W_back = 192
            background = 255 * np.ones((H_back, W_back), dtype=np.uint8)
            y1 = int(H_back//2 - gray.shape[0]/2)
            y2 = int(H_back//2 - gray.shape[0]/2)+H
            x1 = int(W_back//2 - gray.shape[1]/2)
            x2 = int(W_back//2 - gray.shape[1]/2)+W
            background[y1:y2, x1:x2] = gray

            # 画像表示
            plt.imshow(background, cmap="gray")
            # plt.tight_layout()
            plt.pause(0.01)
            start = time.time()

            # Evaluation
            while True:
                print("+--------------------------------------------------")        
                print(f"| image:  {count+1} / 150")
                print("+--------------------------------------------------")        
                print('| 5点 ： All read fine.')
                print('| 4点 ： Generally readable, but some text is difficult to read.')
                print('| 3点 ： Some of the text is unreadable.')
                print("| 2点 ： Most of them can't read.")
                print("| 1点 ： I can't read at all.")
                print("+--------------------------------------------------")        
                val = input("Put your score >> ")
                try:
                    if int(val)>=1 and int(val)<= 5:
                        elapsed_time = time.time() - start
                        with open(res_name, 'a') as f:
                            f.write(imgname + ' ' + val + ' {:.4f}\n'.format(elapsed_time))
                        break
                    else:
                        print('****** Please Input score 1~5 *******')
                        continue
                except:
                    print('****** Please Input score 1~5 *******')
                    continue

            plt.close()

    # Finish print
    print('\n')
    print("+-----------------------------------------")
    print('| This question is completed!')
    print("| Your answer is saved in 'result_{}.txt'.".format(qid))
    print("| Please submit your answer to this URL:")
    print("| https://www.dropbox.com/request/rIWq2KDb8yV8hnrJfW62")
    print("| Thank you very much for your cooperation!!")
    print("+-----------------------------------------")


