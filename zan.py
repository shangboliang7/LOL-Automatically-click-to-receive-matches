import time
import pyautogui

def zan(postion):
    if len(postion) == 4:
        left, top, width, height = postion
        center = pyautogui.center((left, top, width, height))
        pyautogui.click(center)
        print("匹配成功")
        time.sleep(9)
        #验证是否有人拒绝对局
        reposition = pyautogui.locateOnScreen('zhuye.png', confidence=0.7, grayscale=False)
        if  reposition:
            print("有人拒绝对局，重新匹配！")
            return False
        else:
            print("游戏已进入！")
            return True



if __name__ == "__main__":
    starTime = time.time()
    time.sleep(1) #准备1秒
    try:
        while True:
            position = pyautogui.locateOnScreen('5.png',confidence=0.5,grayscale=False)
            if position:
                if(zan(position)):
                    print("执行成功退出！")
                    break;
                else:
                    print("有人拒绝，重新匹配")
            else:
                time.sleep(1)
                print("未匹配成功，等待一秒")
            if(time.time()-starTime >= 600):
                print("匹配时间超过10分钟，退出")
                break;
    except Exception as e:
        print("匹配失败：失败原因: %s"%e)