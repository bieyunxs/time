import tkinter as tk
from datetime import datetime, timedelta
from tkinter import Toplevel, BooleanVar, Checkbutton, messagebox

# 定义时间段信息
time_periods = [
    {'name': '第一节课', 'start': '8:00', 'end': '8:45'},
    {'name': '第二节课', 'start': '8:55', 'end': '9:40'},
    {'name': '第三节课', 'start': '10:00', 'end': '10:45'},
    {'name': '第四节课', 'start': '10:55', 'end': '11:50'},
    {'name': '第五节课', 'start': '13:50', 'end': '14:35'},
    {'name': '第六节课', 'start': '14:45', 'end': '15:30'},
    {'name': '第七节课', 'start': '15:40', 'end': '16:25'},
    {'name': '第八节课', 'start': '16:35', 'end': '17:20'},
    {'name': '晚自习一', 'start': '18:30', 'end': '19:15'},
    {'name': '晚自习二', 'start': '19:25', 'end': '20:10'},
    {'name': '晚自习三', 'start': '20:20', 'end': '21:30'}
]

# 检查当前时间是否在某个时间段内
def is_in_period(current_time, periods):
    for period in periods:
        period_start = datetime.strptime(period['start'], '%H:%M').time()
        period_end = datetime.strptime(period['end'], '%H:%M').time()
        if period_start <= current_time < period_end:
            return period
    return {'name': '下课时间', 'start': '下课', 'end': '下课'}


# 更新窗口中的时间和剩余时间信息
def update_time_info():
    current_time = datetime.now()
    current_date = current_time.strftime('%Y-%m-%d')
    current_day_of_week = current_time.strftime('%A')

    date_label.config(text=f"日期: {current_date}")
    day_of_week_label.config(text=f"星期: {current_day_of_week}")

    current_time = current_time.time()
    current_period = is_in_period(current_time, time_periods)

    time_label.config(text=f"当前时间: {current_time.strftime('%H:%M:%S')}")

    if current_period['name'] == '下课时间':
        period_label.config(text="当前时间段: 下课时间")
        next_period_index = 0
        for i, period in enumerate(time_periods):
            if period['start'] > current_time.strftime('%H:%M'):
                next_period_index = i
                break

        next_period_start = datetime.strptime(time_periods[next_period_index]['start'], '%H:%M').time()
        wait_time = timedelta(hours=next_period_start.hour - current_time.hour,
                              minutes=next_period_start.minute - current_time.minute,
                              seconds=next_period_start.second - current_time.second)

        # 确保等待时间不为负，并处理跨天的情况
        if wait_time.total_seconds() < 0:
            wait_time = timedelta(hours=24) + wait_time

        hours, remainder = divmod(wait_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        remaining_label.config(text=f"到下一时间段: {minutes:02d} 分 {seconds:02d} 秒")
    else:
        period_label.config(text=f"当前时间段: {current_period['name']} ")
        period_end_time = datetime.strptime(current_period['end'], '%H:%M').time()
        time_remaining_in_period = timedelta(hours=period_end_time.hour - current_time.hour,
                                             minutes=period_end_time.minute - current_time.minute,
                                             seconds=period_end_time.second - current_time.second)

        # 确保剩余时间不为负
        if time_remaining_in_period.total_seconds() < 0:
            time_remaining_in_period = timedelta(seconds=0)

        hours, remainder = divmod(time_remaining_in_period.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        remaining_label.config(text=f"剩余时间: {minutes:02d} 分 {seconds:02d} 秒")

    root.after(500, update_time_info)


# 计算屏幕中心位置
def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (270 / 2))  # 窗口宽度为270
    y_cordinate = int((screen_height / 2) - (240 / 2))  # 窗口高度为240
    window.geometry("+{}+{}".format(x_cordinate, y_cordinate))


root = tk.Tk()  # 创建主窗口
root.title("time 2.0.1.0")
root.geometry("270x240")  # 设置窗口大小
root.configure(bg="white")  # 设置背景颜色为白色
root.resizable(False, False)  # 禁止窗口大小调整

center_window(root)

# 创建标签用于显示日期、星期、时间和剩余时间信息
date_label = tk.Label(root, text="")
date_label.pack(pady=10)
day_of_week_label = tk.Label(root, text="")
day_of_week_label.pack(pady=5)
time_label = tk.Label(root, text="")
time_label.pack(pady=10)
period_label = tk.Label(root, text="")
period_label.pack(pady=10)
remaining_label = tk.Label(root, text="")
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
