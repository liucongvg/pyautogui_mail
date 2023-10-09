import pyautogui
import time
# 打开命令文件（假设命令文件中每行包含一个PyAutoGUI命令）
time.sleep(15)
file_path = '/home/ctyun/Desktop/mouse_log.txt'
try:
    with open(file_path, 'r') as file:
        commands = file.readlines()
except FileNotFoundError:
    print(f"文件 '{file_path}' 未找到.")
    exit(1)

# 执行PyAutoGUI命令
while True:
    for command in commands:
        try:
            # 剥离命令字符串两端的空白字符并执行命令
            command = command.strip()
            print('command:' + command)
            eval(command)
        except Exception as e:
            print(f"执行命令 '{command}' 时出错: {e}")

    print("命令执行完成。")



























