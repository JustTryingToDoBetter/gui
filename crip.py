import wx

class ClockApp(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, title='Pomodoro Timer', size=(400, 600))
        self.panel = wx.Panel(self.frame)
        self.panel.SetBackgroundColour('#1C1C1C')  # Dark background color

        # Welcome message
        welcome_text = wx.StaticText(self.panel, label="Start feeling warm!", style=wx.ALIGN_CENTER)
        welcome_text.SetForegroundColour('#00FF00')  # Neon green text color

        # Focus Button
        focus_button = wx.Button(self.panel, label="Focus", size=(100, 30))
        focus_button.SetForegroundColour('#000000')  # Set text color to black
        focus_button.SetBackgroundColour('#39FF14')  # Neon green background
        focus_button.SetWindowStyle(wx.NO_BORDER)  # Frameless button

        # Timer display
        self.time_display = wx.StaticText(self.panel, label="25:00", style=wx.ALIGN_CENTER)
        self.time_display.SetForegroundColour('#FFFFFF')  # Set text color to white
        self.time_display.SetBackgroundColour('#556B2F')  # Army green background
        self.time_display.SetSize((200, 100))
        self.time_display.SetWindowStyle(wx.BORDER_SIMPLE)
        
        # Start button
        start_button = wx.Button(self.panel, label="Fire up!", size=(100, 30))
        start_button.SetForegroundColour('#000000')  # Set text color to black
        start_button.SetBackgroundColour('#39FF14')  # Neon green background
        start_button.SetWindowStyle(wx.NO_BORDER)  # Frameless button
        start_button.Bind(wx.EVT_BUTTON, self.on_start)

        # Use sizers for layout management
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Welcome message alignment
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer.AddStretchSpacer()
        top_sizer.Add(welcome_text, 0, wx.TOP | wx.ALIGN_CENTER, 10)
        top_sizer.AddStretchSpacer()
        main_sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        
        # Focus button alignment
        focus_sizer = wx.BoxSizer(wx.HORIZONTAL)
        focus_sizer.AddStretchSpacer()
        focus_sizer.Add(focus_button, 0, wx.CENTER)
        focus_sizer.AddStretchSpacer()
        main_sizer.Add(focus_sizer, 0, wx.EXPAND | wx.TOP, 20)

        # Timer display alignment
        main_sizer.AddStretchSpacer()
        timer_sizer = wx.BoxSizer(wx.HORIZONTAL)
        timer_sizer.AddStretchSpacer()
        timer_sizer.Add(self.time_display, 0, wx.CENTER)
        timer_sizer.AddStretchSpacer()
        main_sizer.Add(timer_sizer, 0, wx.EXPAND | wx.TOP, 10)
        
        # Start button alignment
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddStretchSpacer()
        button_sizer.Add(start_button, 0, wx.CENTER)
        button_sizer.AddStretchSpacer()
        main_sizer.Add(button_sizer, 0, wx.EXPAND | wx.TOP, 10)
        main_sizer.AddStretchSpacer()
        
        self.panel.SetSizer(main_sizer)
        self.frame.Show()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_clock, self.timer)
        self.remaining_time = 25 * 60  # 25 minutes in seconds

        return True

    def on_start(self, event):
        self.remaining_time = 25 * 60  # Reset to 25 minutes
        self.timer.Start(1000)  # Timer will trigger every second

    def update_clock(self, event):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            minutes, seconds = divmod(self.remaining_time, 60)
            self.time_display.SetLabel(f"{minutes:02}:{seconds:02}")
        else:
            self.timer.Stop()
            self.time_display.SetLabel("Time's up!")

if __name__ == '__main__':
    app = ClockApp()
    app.MainLoop()
