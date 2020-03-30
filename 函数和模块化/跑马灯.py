import os
import time

def main():
    content ='少年抬头，仰望明天。仰望，就有希望。'
    while True:
        # 清理屏幕上的输出
        os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] +content[0]

if __name__ == '__main__':
    main()