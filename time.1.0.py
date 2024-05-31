# import tkinter as tk
# from datetime import datetime, timedelta
#
# # 定义时间段信息
# time_periods = [
#     {'name': '第一节课', 'start': '8:00', 'end': '8:45'},
#     {'name': '第二节课', 'start': '8:55', 'end': '9:40'},
#     {'name': '第三节课', 'start': '10:00', 'end': '10:45'},
#     {'name': '第四节课', 'start': '10:55', 'end': '11:40'},
#     {'name': '第五节课', 'start': '13:50', 'end': '14:35'},
#     {'name': '第六节课', 'start': '14:45', 'end': '15:30'},
#     {'name': '第七节课', 'start': '15:40', 'end': '16:25'},
#     {'name': '第八节课', 'start': '16:35', 'end': '17:20'},
#     {'name': '晚自习一', 'start': '18:30', 'end': '19:15'},
#     {'name': '晚自习二', 'start': '19:25', 'end': '20:10'},
#     {'name': '晚自习三', 'start': '20:20', 'end': '21:30'}
# ]
#
#
# # 检查当前时间是否在某个时间段内
# def is_in_period(current_time, periods):
#     for period in periods:
#         period_start = datetime.strptime(period['start'], '%H:%M').time()
#         period_end = datetime.strptime(period['end'], '%H:%M').time()
#         if period_start <= current_time < period_end:
#             return period
#
#
# # 计算距离下一个时间段开始还有多久
# def calculate_next_period_time(current_time, periods):
#     next_period = None
#     min_delta = timedelta.max
#     for period in periods:
#         period_start = datetime.strptime(period['start'], '%H:%M').time()
#         if period_start > current_time:
#             delta = timedelta(hours=period_start.hour - current_time.hour,
#                               minutes=period_start.minute - current_time.minute,
#                               seconds=0)
#             if delta < min_delta:
#                 min_delta = delta
#                 next_period = period
#     return next_period, min_delta
#
#
# # 更新窗口中的时间和剩余时间信息
# def update_time_info():
#     current_time = datetime.now().time()
#     current_period = is_in_period(current_time, time_periods)
#     next_period, time_remaining = calculate_next_period_time(current_time, time_periods)
#
#     time_label.config(text=f"当前时间: {current_time.strftime('%H:%M:%S')}")
#     period_label.config(text=f"当前时间段: {current_period['name']}")
#
#     if next_period is None:
#         # 当前时间在所有时间段之外，以“下课”为基准计算剩余时间
#         time_remaining = timedelta(0)
#         period_label.config(text=f"当前时间段: 下课")
#
#     remaining_label.config(text=f"距离下一时间段开始还有: {time_remaining.total_seconds() // 60:.0f} 分钟")
#
#     root.after(1000, update_time_info)  # 每秒更新一次时间信息
#
#
# # 创建主窗口
# root = tk.Tk()
# root.title("时间安排")
# root.geometry("300x150")
# root.configure(bg="white")  # 设置背景颜色为白色
#
# # 创建标签用于显示时间和剩余时间信息
# time_label = tk.Label(root, text="")
# time_label.pack(pady=10)
#
# period_label = tk.Label(root, text="")
# period_label.pack(pady=10)
#
# remaining_label = tk.Label(root, text="")
# remaining_label.pack(pady=10)
#
# # 初始化时间信息
# update_time_info()
#
# # 进入主循环
# root.mainloop()


#
# import tkinter as tk
# from datetime import datetime, timedelta
#
# # 定义时间段信息
# time_periods = [
#     {'name': '第一节课', 'start': '8:00', 'end': '8:45'},
#     {'name': '第二节课', 'start': '8:55', 'end': '9:40'},
#     {'name': '第三节课', 'start': '10:00', 'end': '10:45'},
#     {'name': '第四节课', 'start': '10:55', 'end': '11:40'},
#     {'name': '第五节课', 'start': '13:50', 'end': '14:35'},
#     {'name': '第六节课', 'start': '14:45', 'end': '15:30'},
#     {'name': '第七节课', 'start': '15:40', 'end': '16:25'},
#     {'name': '第八节课', 'start': '16:35', 'end': '17:20'},
#     {'name': '晚自习一', 'start': '18:30', 'end': '19:15'},
#     {'name': '晚自习二', 'start': '19:25', 'end': '20:10'},
#     {'name': '晚自习三', 'start': '20:20', 'end': '21:30'}
# ]
#
#
# # 检查当前时间是否在某个时间段内
# def is_in_period(current_time, periods):
#     for period in periods:
#         period_start = datetime.strptime(period['start'], '%H:%M').time()
#         period_end = datetime.strptime(period['end'], '%H:%M').time()
#         if period_start <= current_time < period_end:
#             return period
#     # 当前时间在所有时间段之外，返回一个表示“下课时间”的字典
#     return {'name': '下课时间', 'start': '下课', 'end': '下课'}
#
#
# # 计算距离下一个时间段开始还有多久
# def calculate_next_period_time(current_time, periods):
#     next_period = None
#     min_delta = timedelta.max
#     for period in periods:
#         period_start = datetime.strptime(period['start'], '%H:%M').time()
#         if period_start > current_time:
#             delta = timedelta(hours=period_start.hour - current_time.hour,
#                               minutes=period_start.minute - current_time.minute,
#                               seconds=0)
#             if delta < min_delta:
#                 min_delta = delta
#                 next_period = period
#     return next_period, min_delta
#
#
# # 更新窗口中的时间和剩余时间信息
# def update_time_info():
#     current_time = datetime.now().time()
#     current_period = is_in_period(current_time, time_periods)
#     next_period, time_remaining = calculate_next_period_time(current_time, time_periods)
#
#     time_label.config(text=f"当前时间: {current_time.strftime('%H:%M:%S')}")
#
#     if current_period['name'] == '下课时间':
#         period_label.config(text="当前时间段: 下课时间")
#         remaining_label.config(text="")  # 清空剩余时间显示
#     else:
#         period_label.config(
#             text=f"当前时间段: {current_period['name']} ")
#         period_end_time = datetime.strptime(current_period['end'], '%H:%M').time()
#         time_remaining_in_period = timedelta(hours=period_end_time.hour - current_time.hour,
#                                              minutes=period_end_time.minute - current_time.minute,
#                                              seconds=period_end_time.second - current_time.second)
#         hours, remainder = divmod(time_remaining_in_period.seconds, 3600)
#         minutes, seconds = divmod(remainder, 60)
#         remaining_label.config(text=f"剩余时间: {minutes:02d} 分 {seconds:02d} 秒")
#
#     root.after(1000, update_time_info)  # 每秒更新一次时间信息

#
# # 创建主窗口
# root = tk.Tk()
# root.title("时间安排")
# root.geometry("300x150")
# root.configure(bg="white")  # 设置背景颜色为白色
#
# # 创建标签用于显示时间和剩余时间信息
# time_label = tk.Label(root, text="")
# time_label.pack(pady=10)
#
# period_label = tk.Label(root, text="")
# period_label.pack(pady=10)
#
# remaining_label = tk.Label(root, text="")
# remaining_label.pack(pady=10)
#
# # 初始化时间信息
# update_time_info()
#
# # 进入主循环
# root.mainloop()

#
# import tkinter as tk
# from datetime import datetime, timedelta
#
# # 定义时间段信息
# time_periods = [
#     {'name': '第一节课', 'start': '8:00', 'end': '8:45'},
#     {'name': '第二节课', 'start': '8:55', 'end': '9:40'},
#     {'name': '第三节课', 'start': '10:00', 'end': '10:45'},
#     {'name': '第四节课', 'start': '10:55', 'end': '11:40'},
#     {'name': '第五节课', 'start': '13:50', 'end': '14:35'},
#     {'name': '第六节课', 'start': '14:45', 'end': '15:30'},
#     {'name': '第七节课', 'start': '15:40', 'end': '16:25'},
#     {'name': '第八节课', 'start': '16:35', 'end': '17:20'},
#     {'name': '晚自习一', 'start': '18:30', 'end': '19:15'},
#     {'name': '晚自习二', 'start': '19:25', 'end': '20:10'},
#     {'name': '晚自习三', 'start': '20:20', 'end': '21:30'}
# ]
#
#
# # 检查当前时间是否在某个时间段内
# def is_in_period(current_time, periods):
#     for period in periods:
#         period_start = datetime.strptime(period['start'], '%H:%M').time()
#         period_end = datetime.strptime(period['end'], '%H:%M').time()
#         if period_start <= current_time < period_end:
#             return period
#     return {'name': '下课时间', 'start': '下课', 'end': '下课'}
#
#
# # 更新窗口中的时间和剩余时间信息
# def update_time_info():
#     current_time = datetime.now().time()
#     current_period = is_in_period(current_time, time_periods)
#
#     time_label.config(text=f"当前时间: {current_time.strftime('%H:%M:%S')}")
#
#     if current_period['name'] == '下课时间':
#         period_label.config(text="当前时间段: 下课时间")
#         next_period_start = datetime.strptime(time_periods[0]['start'], '%H:%M').time()
#         if next_period_start > current_time:
#             # 计算到下一个时间段的等待时间，但排除跨天
#             wait_time = timedelta(hours=next_period_start.hour - current_time.hour,
#                                   minutes=next_period_start.minute - current_time.minute,
#                                   seconds=next_period_start.second - current_time.second)
#             if wait_time.total_seconds() < 0:
#                 wait_time = timedelta(hours=24) + wait_time
#             hours, remainder = divmod(wait_time.seconds, 3600)
#             minutes, seconds = divmod(remainder, 60)
#             remaining_label.config(text=f"到下一时间段: {hours:02d} 小时 {minutes:02d} 分")
#         else:
#             remaining_label.config(text="")  # 如果已经过了下个时间段，清空显示
#     else:
#         period_label.config(text=f"当前时间段: {current_period['name']} ")
#         period_end_time = datetime.strptime(current_period['end'], '%H:%M').time()
#         time_remaining_in_period = timedelta(hours=period_end_time.hour - current_time.hour,
#                                              minutes=period_end_time.minute - current_time.minute,
#                                              seconds=period_end_time.second - current_time.second)
#
#         # 确保剩余时间不为负
#         if time_remaining_in_period.total_seconds() < 0:
#             time_remaining_in_period = timedelta(seconds=0)
#
#         hours, remainder = divmod(time_remaining_in_period.seconds, 3600)
#         minutes, seconds = divmod(remainder, 60)
#         remaining_label.config(text=f"剩余时间: {minutes:02d} 分 {seconds:02d} 秒")
#
#     root.after(500, update_time_info)  # 每500毫秒更新一次时间信息
#
#
# # 创建主窗口
# root = tk.Tk()
# root.title("time")
# root.geometry("300x150")
# root.configure(bg="white")  # 设置背景颜色为白色
#
# # 创建标签用于显示时间和剩余时间信息
# time_label = tk.Label(root, text="")
# time_label.pack(pady=10)
#
# period_label = tk.Label(root, text="")
# period_label.pack(pady=10)
#
# remaining_label = tk.Label(root, text="")
# remaining_label.pack(pady=10)
#
# # 初始化时间信息
# update_time_info()
#
# # 进入主循环
# root.mainloop()
