import time as tm

#每个位置可交换的位置集合
g_dict_shifts = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5],
                 3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
                 6:[3,7],  7:[4,6,8], 8:[5,7]}

def swap_chr(a, i, j):
    if i > j:
        i, j = j, i
    if i == j:
        return a
    #得到ij交换后的数组
    b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
    return b

def isSolve(srcLayout, destLayout):
    # 先进行判断srcLayout和destLayout逆序值是否同是奇数或偶数
    # 这是判断起始状态是否能够到达目标状态，同奇同偶时才是可达
    src = 0;
    dest = 0
    for i in range(1, 9):
        fist = 0
        for j in range(0, i):
            if srcLayout[j] > srcLayout[i] and srcLayout[i] != '0':  # 0是false,'0'才是数字
                fist = fist + 1
        src = src + fist

    for i in range(1, 9):
        fist = 0
        for j in range(0, i):
            if destLayout[j] > destLayout[i] and destLayout[i] != '0':
                fist = fist + 1
        dest = dest + fist
    if (src % 2) != (dest % 2):  # 一个奇数一个偶数，不可达
        return -1


def sovleMethod(srcLayout, destLayout):
    # 初始化字典
    g_dict_layouts = {}
    g_dict_layouts[srcLayout] = -1
    stack_layouts = []
    stack_layouts.append(srcLayout)  # 当前状态存入列表
    bFound = False
    while len(stack_layouts) > 0:
        # 广度搜索
        curLayout = stack_layouts.pop(0)  # 出队
        if curLayout == destLayout:  # 判断当前状态是否为目标状态
            break

        # 寻找0 的位置。
        ind_slide = curLayout.index("0")
        lst_shifts = g_dict_shifts[ind_slide]  # 当前可进行交换的位置集合

        for nShift in lst_shifts:
            newLayout = swap_chr(curLayout, nShift, ind_slide)
            if g_dict_layouts.get(newLayout) == None:  # 判断交换后的状态是否已经查询过
                g_dict_layouts[newLayout] = curLayout
                stack_layouts.append(newLayout)  # 存入集合

    lst_steps = []
    lst_steps.append(curLayout)
    while g_dict_layouts[curLayout] != -1:  # 存入路径
        curLayout = g_dict_layouts[curLayout]
        lst_steps.append(curLayout)
    lst_steps.reverse()
    return lst_steps

def solvePuzzle_depth(srcLayout, destLayout):
    if isSolve(srcLayout, destLayout) == -1:
        return 1,sovleMethod(srcLayout, destLayout)
    else:
        return 0,sovleMethod(srcLayout, destLayout)

def getAnswer(srcLayout, destLayout, step, swap):
    mark = 0
    mySwap = [0, 0]
    mySwap[0] = swap[0]
    mySwap[1] = swap[1]
    isChange, lst_steps = solvePuzzle_depth(srcLayout, destLayout)
    ans_str = ''  # 操作序列
    if len(lst_steps) > step + 1:
        rList = []
        rList.append(lst_steps[step])

    if (len(lst_steps) > step + 1 and isChange == 1):
        mark = 1
        lst_steps[step] = swap_chr(lst_steps[step], swap[0] - 1, swap[1] - 1)  # 进行强制交换
        BchangeStr = lst_steps[step]
        '''
        print("调换前：" + rList[0])
        print("调换后：" + lst_steps[step - 1])
        '''
        flagChange = isSolve(lst_steps[step], destLayout)
        if flagChange == -1:
            # print('-1')
            i = lst_steps[step].index('0') + 1
            if i == 9:
                mySwap[0] = 8
                mySwap[1] = 6
            elif i == 1:
                mySwap[0] = 2
                mySwap[1] = 4
            else:
                mySwap[0] = i + 1
                mySwap[1] = i - 1
            lst_steps[step] = swap_chr(lst_steps[step], mySwap[0] - 1, mySwap[1] - 1)
            BchangeStr = lst_steps[step]
        else:
            mySwap = []

        isChange1, lst_steps1 = solvePuzzle_depth(lst_steps[step], destLayout)
        lst_steps = lst_steps[:step] + rList + lst_steps1[1:]
    elif (len(lst_steps) > step and isChange == 0):
        if swap[0] == swap[1]:
            mySwap = []
        elif lst_steps[step][swap[0] - 1] == '0' or lst_steps[step][swap[1] - 1] == '0':
            if abs(swap[0] - swap[1]) % 2 == 1:
                lst_steps[step] = swap_chr(lst_steps[step], swap[0] - 1, swap[1] - 1)
                BchangeStr = lst_steps[step]
                lst_steps1 = sovleMethod(lst_steps[step - 1], destLayout)
                lst_steps = lst_steps[:step] + rList + lst_steps1[1:]
                mySwap = []
                mark = 1
            else:
                mySwap[0] = swap[0]
                mySwap[1] = swap[1]

    length = len(lst_steps) - 1
    #获得操作序列
    for i in range(length):
        if mark == 1 and i == step:
            if lst_steps[i + 1].index('0') - BchangeStr.index('0') == -3:
                ans_str = ans_str + 'w'
            elif lst_steps[i + 1].index('0') - BchangeStr.index('0') == 3:
                ans_str = ans_str + 's'
            elif lst_steps[i + 1].index('0') - BchangeStr.index('0') == -1:
                ans_str = ans_str + 'a'
            elif lst_steps[i + 1].index('0') - BchangeStr.index('0') == 1:
                ans_str = ans_str + 'd'
        elif lst_steps[i + 1].index('0') - lst_steps[i].index('0') == -3:
            ans_str = ans_str + 'w'
        elif lst_steps[i + 1].index('0') - lst_steps[i].index('0') == 3:
            ans_str = ans_str + 's'
        elif lst_steps[i + 1].index('0') - lst_steps[i].index('0') == -1:
            ans_str = ans_str + 'a'
        elif lst_steps[i + 1].index('0') - lst_steps[i].index('0') == 1:
            ans_str = ans_str + 'd'
    return  ans_str, mySwap, lst_steps


if __name__ == "__main__":
    #测试数据输入格式
    srcLayout  = "801462935"        #初始状态
    destLayout = "123456089"        #目标状态
    step = 1
    swap = [1,3]
    ans_str, mySwap, lst_steps = getAnswer(srcLayout, destLayout, step, swap)
    print(ans_str,mySwap)
    for nIndex in range(len(lst_steps)):
        print("step #" + str(nIndex))
        print(lst_steps[nIndex][:3])
        print(lst_steps[nIndex][3:6])
        print(lst_steps[nIndex][6:])
    print('移动步数：%d' % len(lst_steps))