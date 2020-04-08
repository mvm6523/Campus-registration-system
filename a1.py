import wx
import datetime



class MyFrame(wx.Frame):
    def __init__(self,  parent,  id):
        wx.Frame.__init__(self,  parent,  id,  '用户登录',  size=(400,  300))
        # 创建面板
        panel = wx.Panel(self)

        # 创建“确定”和“取消”按钮, 并绑定事件
        self.bt_confirm = wx.Button(panel,  label='进入校园')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel,  label='离开校园')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        # 创建文本，左对齐        
        self.title = wx.StaticText(panel,  label="请输入姓名和学号")
        self.label_user = wx.StaticText(panel,  label="姓名:")
        self.text_user = wx.TextCtrl(panel,  style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel,  label="学号:")
        self.text_password = wx.TextCtrl(panel,  style=wx.TE_PASSWORD)
        # 添加容器，容器中控件按横向并排排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user,  proportion=0,  flag=wx.ALL,  border=5)
        hsizer_user.Add(self.text_user,  proportion=1,  flag=wx.ALL,  border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd,  proportion=0,  flag=wx.ALL,  border=5)
        hsizer_pwd.Add(self.text_password,  proportion=1,  flag=wx.ALL,  border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        hsizer_button.Add(self.bt_cancel,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title,  proportion=0,  flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, 
                        border=15)
        vsizer_all.Add(hsizer_user,  proportion=0,  flag=wx.EXPAND | wx.LEFT | wx.RIGHT,  border=45)
        vsizer_all.Add(hsizer_pwd,  proportion=0,  flag=wx.EXPAND | wx.LEFT | wx.RIGHT,  border=45)
        vsizer_all.Add(hsizer_button,  proportion=0,  flag=wx.ALIGN_CENTER | wx.TOP,  border=15)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self, event):
        """ 点击进入校园按钮，执行方法 """
        message = ""
        name = self.text_user.GetValue()     # 获取输入的姓名
        no = self.text_password.GetValue()  # 获取输入的学号
        time1 = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
        if name == "" or no == "":    # 判断姓名或学号是否为空
            message = '姓名或学号不能为空'
        else:
            message = '姓名：'+name+' 学号：'+no+' 进入校园时间：'+time1_str            # 用户名或密码错误  
            
        wx.MessageBox(message)                        # 弹出提示框          

    def OnclickCancel(self, event):  
        """ 点击离开校园按钮，执行方法 """
        message = ""
        name = self.text_user.GetValue()     # 获取输入的姓名
        no = self.text_password.GetValue()  # 获取输入的学号
        time1 = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
        if name == "" or no == "":    # 判断姓名或学号是否为空
            message = '姓名或学号不能为空'
        else:
            message = '姓名：'+name+' 学号：'+no+' 离开校园时间：'+time1_str            # 用户名或密码错误 
    
        


if __name__ == '__main__':
    app = wx.App()                      # 初始化
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数    
    frame.Show()                        # 显示窗口
    app.MainLoop()                      # 调用主循环方法