# coding = utf-8

import tkinter as tk
import time
from selenium import webdriver

root = tk.Tk()
from tkinter.filedialog import (askopenfilename)


def refresh(url, num, time_slot):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    file_link = askopenfilename(title='请选择chrome安装路径')
    driver = webdriver.Chrome(chrome_options=options, executable_path=file_link)
    driver.get(url)
    for i in range(num):
        time.sleep(time_slot)
        driver.refresh()



if __name__ == "__main__":
    url = input("请输入网页链接:\n")
    num = int(input("请输入刷新次数:\n"))
    time_slot = int(input("请输入网页刷新时间间隔："))
    refresh(url, num, time_slot)
