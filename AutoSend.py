import psutil
from uiautomation import *
from pywinauto.application import Application
from keyboard import enter, open_search, typewrite


class AutoSendMsg:
    def __init__(self, app_type, app_path):
        self.app_type = app_type
        # 首先检查是否有微信/QQ进程在运行
        if self.is_process_running(f"{self.app_type}.exe"):
            try:
                # 尝试连接到已经运行的进程
                self.app = Application(backend="uia").connect(path=app_path)
                print(f"已连接到运行中的 {self.app_type}")
                time.sleep(1)
            except Exception as e:
                print(f"连接到 {self.app_type} 失败: {e}")
        else:
            try:
                # 启动新的进程
                self.app = Application(backend="uia").start(app_path)
                print(f"启动了新的 {self.app_type} 实例")
                time.sleep(3)
                enter()  # 登录
                time.sleep(5)  # 等待应用程序启动
            except Exception as e:
                print(f"启动 {self.app_type} 失败: {e}")


    def is_process_running(self, process_name):
        """检查是否有指定的进程正在运行"""
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                return True
        return False

    def page_open(self):  # QQ无法实现这一步，原因不明
        """尝试多种方式来获取主窗口"""

        try:
            # 方式1: 使用应用程序的顶层窗口
            self.wechat_window = self.app.top_window()
            self.wechat_window.set_focus()
            print("使用 top_window 成功激活窗口")
        except Exception as e:
            print(f"使用 top_window 激活窗口失败: {e}")
            try:
                # 方式2: 使用窗口标题的正则表达式匹配
                self.wechat_window = self.app.window(
                    title_re=f".*{self.app_type}.*")  # 匹配包含应用名的窗口标题(但是好像微信和QQ的窗口标题都不叫WeChat/QQ。。)
                self.wechat_window.set_focus()
                print("使用 title_re 成功激活窗口")
            except Exception as e:
                print(f"使用 title_re 激活窗口失败: {e}")
                try:
                    # 方式3: 使用窗口的类名获取
                    if self.app_type == 'WeChat':
                        self.wechat_window = self.app.window(class_name="WeChatMainWndForPC")
                    elif self.app_type == 'QQ':
                        self.wechat_window = self.app.window(
                            class_name="Chrome_RenderWidgetHostHWND")  # 查找窗体发现QQ的窗体类名就叫这个但是还是没用，原因不明
                    self.wechat_window.set_focus()
                    print("使用 class_name 成功激活窗口")
                except Exception as e:
                    print(f"使用 class_name 激活窗口失败: {e}")

        time.sleep(1)  # 确保窗口获得焦点


    def send_message(self, friend_name, message, send_time):
        print(f"{send_time}到了，即将给好友{friend_name}发送消息")
        self.page_open()
        # 在搜索框中输入好友昵称
        open_search()
        typewrite(friend_name)
        time.sleep(1)
        enter()

        # 输入并发送消息
        typewrite(message)
        time.sleep(1)
        enter()
        print(f"已在{send_time}给好友{friend_name}发送以下消息:{message}")
