# import module
import wx
from ATShutdownDialog import ATShutdownDialog

# buat objek aplikasi
app = wx.App()

# buat dialog
dialog = ATShutdownDialog()

# tampilkan
dialog.ShowModal()

if dialog.idleSensor != None:
    dialog.idleSensor.stopService()
