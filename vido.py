import cv2
'''
定义保存图片的函数
image：要保存的图片
addr：图片的地址和名称信息
num图片名称的后缀，使用int类型来计数
'''
def save_image(image,addr,num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address,image)
#   读取视频文件
vode = cv2.VideoCapture("1.mp4")
#   读帧
success,frame = vode.read()
#   初始化变量
i = 0   # 帧计数
j = 0   # 图片计数
timeF = 25  #   每隔57帧（一秒）保存一张图片
# 使用循环进行图片的保存
while success:
    i = i + 1
    if (i % timeF == 0):
        j = i +1
        save_image(frame, './image_', j)
        print('save image:',j)
    success,frame = vode.read()
