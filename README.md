最近因为某些原因需要在特定时间给别人发送消息，本以为微信会有自带定时发消息功能结果发现没有，就想着用Python自己写一个定时发消息的脚本。
初步了解了下相关的API好像用不了了，于是想到可以用pynput库模拟按键, pywinauto、uiautomation库实现界面的自动化。
### 环境准备:用到的库有schedule, psutil, uiautomation, pywinauto, pynput
pip install -r requirements.txt

### 使用方法
在main.py中将exe文件路径`wechat_path/qq_path`修改为自己的路径，自行设定发送时间`send_time`、好友`friend_name`和消息`message`后直接运行`main.py`，详见代码注释

### 存在的问题
QQ无法自动获取窗口，原因不明，需要自己保持窗口在顶层，微信没问题
改成小写qq就可以了，不过又改回大写也可以正常执行了，莫名其妙的
