import simpleguitk as simplegui
import random
import pygame
import easygui
from tkinter import *
from tkinter import scrolledtext



baymax = simplegui.load_image("https://images.cnblogs.com/cnblogs_com/czjlfe566/1842405/o_201019103614haha.jpg")
width = 900
height = 900+100    #多的100来存放步数
# 定义图像块的边长
image_size = width / 3
# 定义图像块的坐标列表
all_coordinates = [[image_size * 0.5, image_size * 0.5], [image_size * 1.5, image_size * 0.5],
                   [image_size * 2.5, image_size * 0.5], [image_size * 0.5, image_size * 1.5],
                   [image_size * 1.5, image_size * 1.5], [image_size * 2.5, image_size * 1.5],
                   [image_size * 0.5, image_size * 2.5], [image_size * 1.5, image_size * 2.5],
                   None
                   ]
# 棋盘的行列
ROWS = 3
COLS = 3

# 棋盘步数
steps = 0
flag = 0
# 保存所有图像块的列表
board = [[None, None, None], [None, None, None], [None, None, None]]

# 定义一个图像块的类
class Square:

    def __init__(self, coordinate):
        self.center = coordinate   #把坐标赋值给图像块中心,order_id
    #对图片进行裁剪
    def draw(self, canvas, board_pos):
        canvas.draw_image(baymax, self.center, [image_size, image_size],
                          [(board_pos[1] + 0.5) * image_size, (board_pos[0] + 0.5) * image_size]
                          , [image_size, image_size])
        #drawImage(image, dx, dy, dw, dh)
        #第一个参数image可以用HTMLImageElement，HTMLCanvasElement或者HTMLVideoElement作为参数。
        #  dx和dy是image在canvas中定位的坐标值；
        #  dw和dh是image在canvas中即将绘制区域（相对dx和dy坐标的偏移量）的宽度和高度值；
        #  sx和sy是image所要绘制的起始位置，sw和sh是image所要绘制区域（相对image的sx和sy坐标的偏移量）的宽度和高度值。


def init_board():
    """对每个小方格，创建方块对象"""

    # 随机打乱列表
    random.shuffle(all_coordinates)
    # 填充并且拼接图版

    for i in range(ROWS):
        for j in range(COLS):
            idx = i * ROWS + j
            square_center = all_coordinates[idx]   #图形中心坐标
            if square_center is None:
                board[i][j] = None
            else:
                board[i][j] = Square(square_center)


def play_game():
    """重置游戏"""
    global steps
    steps = 0
    init_board()


def play_music():
    """打开音乐"""
    # 音乐的路径
    global flag
    flag=(flag+1)%4
    if flag==1:
        file = r'bgm1.mp3'
    if flag==2:
        file = r'bgm2.mp3'
    if flag==3:
        file = r'bgm3.mp3'
    if flag==0:
        file = r'bgm4.mp3'
    # 初始化
    pygame.mixer.init()
    # 加载音乐文件
    track = pygame.mixer.music.load(file)
    # 开始播放音乐流
    pygame.mixer.music.play()


def play_Closemusic():
    """close音乐"""
    pygame.mixer.music.stop()
def play_Close():
    sys.exit()

def draw(canvas):
    """画界面上的元素"""
    # 画下方图片
    canvas.draw_image(baymax, [width / 2, height / 2], [width+100, height+100], [50, width + 50], [98, 98])
    # 画下方步数
    canvas.draw_text("步数: " + str(steps), [400, 980], 22, 'black')
    # 绘制游戏界面各元素
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None:
                board[i][j].draw(canvas, [i, j])


def mouse_click(pos):
    """鼠标点击事件"""
    global steps
    # r为行数，c为列数
    r = int(pos[1] // image_size)
    c = int(pos[0] // image_size)

    if r < 3 and c < 3:
        # 点击到空白位置
        if board[r][c] is None:
            return
        else:
            # 依次检查当前图像位置的上下左右是否有空位置
            current_square = board[r][c]
            # 判断上面
            if r - 1 >= 0 and board[r - 1][c] is None:
                board[r][c] = None
                board[r - 1][c] = current_square
                #print(board[r-1][c].center)
                steps += 1
            # 判断下面
            elif r + 1 <= 2 and board[r + 1][c] is None:
                board[r][c] = None
                board[r + 1][c] = current_square
                #print(board[r+1][c].center)
                steps += 1
            # 判断在左边
            elif c - 1 >= 0 and board[r][c - 1] is None:
                board[r][c] = None
                board[r][c - 1] = current_square
                steps += 1
            # 判断在右边
            elif c + 1 <= 2 and board[r][c + 1] is None:
                board[r][c] = None
                board[r][c + 1] = current_square
                #print(board[r][c+1].center)
                steps += 1
            if win():
                easygui.msgbox("成功还原","华容道","OK")
                with open("old.txt", "a") as f:     #把数字的内容存入oldTXT中，之后对old里的数据进行排序
                    shuchu=str(steps)
                    f.write(shuchu)
                    f.write('\n')
            elif no_have():
                 easygui.msgbox("恭喜你把坏运气用掉了！","华容道","好运来")

def win():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None and board[i][j].center!=[150+300*j,150+i*300]:
                return False
    return True
def no_have():
    anss=0
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None and board[i][j].center==[150+300*j,150+i*300]:
                anss=anss+1
    print(anss)
    if anss==6  and board[2][0].center==[450,750] and board[2][1].center==[150,750]:
                 return True

def history_score():
    txtsort()
    window = Tk()
    window.title("成绩排名")
    window.geometry("600x600")
    sda = scrolledtext.ScrolledText(window, width=38, height=20, font=("宋体",20))
    sda.place(x=30, y=30)
    f = open("shuchu.txt", "r")
    s = f.read()
    sda.insert(END, s)
    with open("shuchu.txt", 'r+') as file:
         file.truncate(0)
    window.mainloop()

def txtsort():#把保存有步数的txt文件里的步数放到列表进行排序
    file = open("old.txt", "r")
    ar = []
    arr = []
    count = 1
    flag = 0
    for line in file:
        if '\n' in line and flag == 0:
            flag = 1
            continue
        if '\n' in line:
            idx = line.index('\n')
        else:
            continue
        temp = int(line[:idx])
        ar.append(temp)
    for i in ar:
        if i not in arr:
            arr.append(i)
    arr.sort()
    file = open("shuchu.txt", 'a') #在列表里完成排序之后输出到txt里
    for i in range(len(arr)):
        s = str(arr[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = 'NO.' + str(count) + ':' + s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
        count = count + 1
    file.close()
    print("保存文件成功")



frame = simplegui.create_frame('数字九空格', width, height)
frame.set_canvas_background('white')
# 绘制界面
frame.set_draw_handler(draw)
# 创建窗口，绑定事件，设置大小
frame.add_button('重新开始', play_game, 60)
frame.add_button('音乐/切歌', play_music, 60)
frame.add_button('关闭音乐', play_Closemusic, 60)
frame.add_button('退出', play_Close, 60)
frame.add_button('历史成绩', history_score, 60)
# 注册鼠标事件
frame.set_mouseclick_handler(mouse_click)
# 初始化游戏
play_game()
# 启动框架
frame.start()