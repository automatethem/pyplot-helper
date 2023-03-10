from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#matplotlib 패키지 한글 깨짐 처리 시작
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        #!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        #!mv malgun.ttf /usr/share/fonts/truetype/
        #import matplotlib.font_manager as fm 
        #fm._rebuild() 
        plt.rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결
#matplotlib 패키지 한글 깨짐 처리 끝

def draw_rect(image, point1, point2):
    plt.figure(figsize=(16, 10))
    #fig, ax = plt.subplots(nrows=1, ncols=1)
    fig = plt.gcf()
    ax = plt.gca()
    plt.imshow(image)
    x1, y1 = point1
    x2, y2 = point2
    ax.add_patch(
        patches.Rectangle(
            (x1, y1), x2 - x1, y2 - y1,
            edgecolor='red',
            facecolor='red',
            linewidth=2,
            fill=False
        )
    )
    plt.xticks([])
    plt.yticks([])
    plt.show()

def draw_label(image, text, point, font_color=(255, 255, 255), font_size=28):
    plt.figure(figsize=(16, 10))
    #fig, ax = plt.subplots(nrows=1, ncols=1)
    fig = plt.gcf()
    ax = plt.gca()
    plt.imshow(image)
    x, y = point
    ax.text(x, y, text)
    plt.xticks([])
    plt.yticks([])
    plt.show()

def draw_rect_with_label(image, point1, point2, text, font_color=(255, 255, 255), font_size=28):
    plt.figure(figsize=(16, 10))
    #fig, ax = plt.subplots(nrows=1, ncols=1)
    fig = plt.gcf()
    ax = plt.gca()
    plt.imshow(image)
    x1, y1 = point1
    x2, y2 = point2
    ax.add_patch(
        patches.Rectangle(
            (x1, y1), x2 - x1, y2 - y1,
            edgecolor='red',
            facecolor='red',
            linewidth=2,
            fill=False
        )
    )
    plt.xticks([])
    plt.yticks([])
    plt.show()

def draw_point(image, point):
    plt.figure(figsize=(16, 10))
    #fig, ax = plt.subplots(nrows=1, ncols=1)
    fig = plt.gcf()
    ax = plt.gca()
    plt.imshow(image)
    x, y = point
    ax.add_patch(
        patches.Circle(
            (x, y),
            edgecolor='red',
            facecolor='red',
            linewidth=2,
            fill=True
        )
    )
    plt.xticks([])
    plt.yticks([])
    plt.show()

#plt.savefig('image.png')
