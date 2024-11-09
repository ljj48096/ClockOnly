import tkinter as tk
from time import strftime

# 创建主窗口
root = tk.Tk()
root.title("系统时间与日期显示")

# 设置初始窗口大小
root.geometry("300x150")

# 创建标签来显示时间
time_label = tk.Label(root, background="black", foreground="white")
time_label.pack(fill="both", expand=True)

# 创建标签来显示日期
date_label = tk.Label(root, background="black", foreground="white")
date_label.pack(fill="both", expand=True)

# 定义更新时间的函数
def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

# 定义更新日期的函数
def update_date():
    current_date = strftime('%Y-%m-%d')
    date_label.config(text=current_date)
    date_label.after(86400000, update_date)

# 初始化上次更新的宽度
last_width = 0
update_threshold = 20  # 最小更新阈值

# 根据窗口宽度调整字体大小
def adjust_font(event):
    global last_width
    current_width = event.width
    # 只有当宽度变化超过阈值时才更新字体大小
    if abs(current_width - last_width) > update_threshold:
        # 更新字体大小
        time_font_size = int(current_width * 0.1)
        date_font_size = int(current_width * 0.05)
        time_label.config(font=("calibri", time_font_size, "bold"))
        date_label.config(font=("calibri", date_font_size))
        # 记录当前宽度
        last_width = current_width

# 绑定窗口大小变化事件
root.bind("<Configure>", adjust_font)

# 初始化时间和日期显示
update_time()
update_date()

if __name__ == '__main__':
    # 运行主循环
    root.mainloop()
