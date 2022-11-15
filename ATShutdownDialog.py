import wx
from BaseDialog import BaseDialog
from IdleSensor import IdleSensor


class ATShutdownDialog (BaseDialog):

    def __init__(self):
        BaseDialog.__init__(self, None)

        self.m_button_toggle_idle_sensor.Bind(
            wx.EVT_BUTTON, self.onButtonToggleIdleSensor)
        self.isEnabled = False
        self.m_button_toggle_idle_sensor.SetLabelText(
            "Idle Sensor is Disabled")

        self.idleSensor = IdleSensor()

    def __del__(self):
        pass

    def onButtonToggleIdleSensor(self, e):
        if self.isEnabled == True:
            self.isEnabled = False
            self.m_button_toggle_idle_sensor.SetLabelText(
                "Idle Sensor is Disabled")
            self.idleSensor.stopService()
        else:
            self.isEnabled = True
            self.m_button_toggle_idle_sensor.SetLabelText(
                "Idle Sensor is Enabled")

            print("service started, waiting for idle in: " +
                  str(self.m_spin_ctrl_shutdown_after.GetTextValue()) + " minutes")

            self.idleSensor.targetTime = int(
                self.m_spin_ctrl_shutdown_after.GetTextValue()) * 60
            self.idleSensor.startService()
