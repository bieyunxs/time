import tkinter as tk
from datetime import datetime, date, time

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
                remaining_label.config(text="本时间段即将结束")
    else:
        # 计算到下一个时间段的开始时间
        nearest_period_start = min((x for x in time_periods if x['start'] > current_time),
                                   key=lambda x: datetime.combine(date.today(), x['start']) - current_datetime,
                                   default={'start': time(0)})
        time_difference = datetime.combine(date.today(), nearest_period_start['start']) - current_datetime
        if time_difference.total_seconds() < 6 * 3600:  # 如果时间差小于6小时
            minutes, seconds = divmod(time_difference.seconds, 60)
            remaining_label.config(text=f"剩余时间: {minutes:02d}:{seconds:02d}")
        else:
            remaining_label.config(text="今天课程已结束")

    root.after(500, update_time_info)  # 每半秒更新一次时间信息


# 创建主窗口
root = tk.Tk()
root.title("time2.0.0.first_ver")
root.geometry("240x210")
root.configure(bg="white")
root.resizable(False, False)

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

# 进入主循环
root.mainloop()
