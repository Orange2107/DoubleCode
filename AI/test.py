import solves
import unittest

class TestFuctions(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("开始测试:")
    @classmethod
    def tearDown(self):
        print("测试结束")

    def test_1(self):
        print("初始状态有解，强制交换后仍有解:")
        srcLayout  = "108462935"        #初始状态
        destLayout = "123456089"        #目标状态
        step = 1
        swap = [1,1]
        ans_str, mySwap, lst_steps = solves.getAnswer(srcLayout, destLayout, step, swap)
        print("初始状态：")
        print(srcLayout)
        print("强制交换：")
        print(swap)
        print("我的交换：")
        print(mySwap)
        print("操作序列：%s"%ans_str)
        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])
        print('移动步数：%d' % len(lst_steps))
    def test_2(self):
        print("初始状态有解，强制交换后无解:")
        srcLayout  = "108462935"        #初始状态
        destLayout = "123456089"        #目标状态
        step = 1
        swap = [1,2]
        ans_str, mySwap, lst_steps = solves.getAnswer(srcLayout, destLayout, step, swap)
        print("初始状态：")
        print(srcLayout)
        print("强制交换：")
        print(swap)
        print("我的交换：")
        print(mySwap)
        print("操作序列：%s"%ans_str)
        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])
        print('移动步数：%d' % len(lst_steps))


    def test_3(self):
        print("初始状态无解，强制交换后有解:")
        srcLayout = "801462935"  # 初始状态
        destLayout = "123456089"  # 目标状态
        step = 1
        swap = [1, 3]
        ans_str, mySwap, lst_steps = solves.getAnswer(srcLayout, destLayout, step, swap)
        print("初始状态：")
        print(srcLayout)
        print("强制交换：")
        print(swap)
        print("我的交换：")
        print(mySwap)
        print("操作序列：%s" % ans_str)
        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])
        print('移动步数：%d' % len(lst_steps))


    def test_4(self):
        print("初始状态无解，强制交换后仍无解:")
        srcLayout = "108462935"  # 初始状态
        destLayout = "123456089"  # 目标状态
        step = 1
        swap = [1, 2]
        ans_str, mySwap, lst_steps = solves.getAnswer(srcLayout, destLayout, step, swap)
        print("初始状态：")
        print(srcLayout)
        print("强制交换：")
        print(swap)
        print("我的交换：")
        print(mySwap)
        print("操作序列：%s" % ans_str)
        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])
        print('移动步数：%d' % len(lst_steps))

if __name__ == "__main__":
    unittest.main()