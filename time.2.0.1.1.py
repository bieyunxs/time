import tkinter as tk
from datetime import datetime, date, time
from tkinter import Toplevel, BooleanVar, Checkbutton, messagebox

# 定义时间段信息
time_periods = [
    {'name': '第一节课', 'start': time(8, 30), 'end': time(9, 15)},
    {'name': '第二节课', 'start': time(9, 25), 'end': time(10, 10)},
    {'name': '第三节课', 'start': time(10, 20), 'end': time(11, 5)},
    {'name': '第四节课', 'start': time(11, 15), 'end': time(11, 50)},
    {'name': '第五节课', 'start': time(13, 50), 'end': time(14, 35)},
    {'name': '第六节课', 'start': time(14, 45), 'end': time(15, 30)},
    {'name': '第七节课', 'start': time(15, 40), 'end': time(16, 25)},
    {'name': '第八节课', 'start': time(16, 35), 'end': time(17, 20)},
    {'name': '晚自习一', 'start': time(18, 30), 'end': time(19, 15)},
    {'name': '晚自习二', 'start': time(19, 25), 'end': time(20, 10)},
    {'name': '晚自习三', 'start': time(20, 20), 'end': time(21, 0)}
]


# 检查当前时间是否在某个时间段内
def is_in_period(current_time, periods):
    for period in periods:
        period_start = period['start']
        period_end = period['end']
        if period_start <= current_time < period_end:
            return period
    return {'name': 'free time', 'start': None, 'end': None}  # 修改为返回None而不是字符串


# 更新窗口中的时间和剩余时间信息
def update_time_info():
    current_datetime = datetime.now()
    current_time = current_datetime.time()
    current_date = current_datetime.date().strftime('%Y-%m-%d')
    current_day_of_week = current_datetime.strftime('%A')

    date_label.config(text=f"日期: {current_date}")
    day_of_week_label.config(text=f"星期: {current_day_of_week}")

    current_period = is_in_period(current_time, time_periods)

    time_label.config(text=f"当前时间: {current_time.strftime('%H:%M:%S')}")

    period_label.config(text=f"当前时间段: {current_period['name']}")

    if current_period['name'] != 'free time':
        if current_period['end']:  # 确保'end'不是None
            period_end = datetime.combine(current_datetime.date(), current_period['end'])
            time_remaining = period_end - current_datetime
            if time_remaining.total_seconds() > 0:
                minutes, seconds = divmod(time_remaining.seconds, 60)
                remaining_label.config(text=f"剩余时间: {minutes:02d}:{seconds:02d}")

    else:
        # 计算到下一个时间段的开始时间
        nearest_period_start = min((x for x in time_periods if x['start'] > current_time),
                                   key=lambda x: datetime.combine(date.today(), x['start']) - current_datetime,
                                   default={'start': time(0)})
        time_difference = datetime.combine(date.today(), nearest_period_start['start']) - current_datetime
        # 如果当日没有了其他时间段，则显示今日剩余时间
        if time_difference.total_seconds() != 0:
            minutes, seconds = divmod(time_difference.seconds, 60)
            remaining_label.config(text=f"当前剩余时间: {minutes:02d}:{seconds:02d}")

    root.after(500, update_time_info)  # 每半秒更新一次时间信息


# 计算屏幕中心位置
def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (270 / 2))  # 窗口宽度为270
    y_cordinate = int((screen_height / 2) - (240 / 2))  # 窗口高度为240
    window.geometry("+{}+{}".format(x_cordinate, y_cordinate))


# 创建主窗口
root = tk.Tk()
root.title("time2.0.1.1")
root.geometry("270x240")
root.configure(bg="white")
root.resizable(False, False)

center_window(root)

# 创建并布局标签
date_label = tk.Label(root, text="", bg="white")
date_label.pack(pady=10)
day_of_week_label = tk.Label(root, text="", bg="white")
day_of_week_label.pack(pady=5)
time_label = tk.Label(root, text="", bg="white")
time_label.pack(pady=10)
period_label = tk.Label(root, text="", bg="white")
period_label.pack(pady=10)
remaining_label = tk.Label(root, text="", bg="white")
remaining_label.pack(pady=10)

# 初始化时间信息
update_time_info()

# 新增设置按钮和设置功能
def open_settings():
    """打开设置窗口，并设置是否始终保持在最上层的复选框"""

    def save_settings():
        """保存设置，并更新窗口是否始终保持在最上层的属性"""
        always_on_top = always_on_top_var.get()
        root.attributes("-topmost", always_on_top)
        if always_on_top:
            messagebox.showinfo("设置已更新", "窗口将始终保持在最上层。")
        else:
            messagebox.showinfo("设置已更新", "窗口将不再始终保持在最上层。")
        settings_win.destroy()

    def cancel_settings():
        """取消设置并关闭设置窗口"""
        settings_win.destroy()

    # 创建设置窗口
    settings_win = Toplevel(root)
    settings_win.title("设置")
    settings_win.geometry("200x100")
    settings_win.configure(bg="white")

    # 是否始终保持在最上层的复选框
    global always_on_top_var
    always_on_top_var = BooleanVar(value=root.attributes("-topmost"))  # 默认值与当前窗口设置一致
    always_on_top_checkbox = Checkbutton(settings_win, text="始终保持在最上层", variable=always_on_top_var)
    always_on_top_checkbox.pack(pady=10)

    # 保存和取消按钮
    save_button = tk.Button(settings_win, text="保存", command=save_settings)
    save_button.pack(side=tk.LEFT, pady=10, padx=10)
    cancel_button = tk.Button(settings_win, text="取消", command=cancel_settings)
    cancel_button.pack(side=tk.RIGHT, pady=10, padx=10)

    # 将设置窗口居中
    center_window(settings_win)


# 在主窗口的创建部分，添加一个设置按钮
settings_button = tk.Button(root, text="设置", command=open_settings)
settings_button.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)  # 放置在右下角


# 进入主循环
root.mainloop()
