import pyautogui


# 点击当前鼠标位置
pyautogui.click()
x =100
y=100
# 点击指定坐标位置
pyautogui.click(x, y)

# 点击指定坐标位置，指定点击次数和点击间隔
pyautogui.click(x, y, clicks=2, interval=0.5)

# 点击指定坐标位置，指定鼠标按钮（可选）
pyautogui.click(x, y, button='left')

# 点击指定坐标位置，同时按下和释放鼠标按钮（可选）
pyautogui.mouseDown(x, y, button='left')
pyautogui.mouseUp(x, y, button='left')


