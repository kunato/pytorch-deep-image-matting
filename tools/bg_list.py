import glob

bg_list = glob.glob('/home/kunato/dataset/coco/train2017/*.jpg')

with open('bg_file_list.txt','w') as f:
    for i in range(0, len(bg_list)):
        # print(img_list[i])
        f.write(bg_list[i]+'\n')

fg_list = glob.glob('/home/kunato/dataset/Matting Dataset/images/Training_set/fg/*.png')

with open('fg_file_list.txt','w') as f:
    for i in range(0, len(fg_list)):
        # print(img_list[i])
        f.write(fg_list[i]+'\n')
