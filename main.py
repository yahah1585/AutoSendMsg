import schedule
import time
from AutoSend import AutoSendMsg

wechat_path = "D:/WeChat/WeChat.exe"  # 微信exe文件路径
qq_path = "D:/QQNT/QQ.exe"  # QQexe文件路径, QQ无法自动打开窗口，需要保持QQ窗口置于顶层
auto_send = AutoSendMsg(app_type='WeChat', app_path=wechat_path)  # app_type:微信——WeChat, QQ——QQ
auto_send.page_open()
friend_name = "好友昵称"  # 好友昵称
message = "这是自动发送的消息"  # 消息内容
send_time = "09:00"  # 设定时间，格式为xx:xx
schedule.every().day.at(send_time).do(auto_send.send_message, friend_name, message, send_time)

""" 设定多个时间点给同一个好友发送同一条消息
send_time = ["09:00", "15:00", "20:00"]
for i, t in enumerate(send_time):
    schedule.every().day.at(t).do(auto_send.send_message, friend_name, message)
"""
""" 设定在同一时间点给多个好友发送同一条消息
friend_name = ["好友1", "好友2", "好友3"]
for i, friend in enumerate(friend_name):
    schedule.every().day.at(send_time).do(auto_send.send_message, friend, message)
"""
""" 设定在不同时间给好友发送不同消息
time_message = {"09:00": "起床了吗", "15:00": "去健身吗", "20:00": "打游戏吗"}
for t, msg in enumerate(time_message):
    schedule.every().day.at(t).do(auto_send.send_message, friend_name, msg)
"""

if __name__ == "__main__":
    # 主循环，保持运行
    while True:
        schedule.run_pending()
        time.sleep(1)
