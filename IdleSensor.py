import threading
import time
import os
from pynput.keyboard import Key, Listener
from pynput import mouse


class KeyboardIdleSensorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = False
        self.idleThread = None

    def run(self):
        self.running = True
        with Listener(
                on_press=self.onPress,
                on_release=self.onRelease) as listener:
            listener.join()

    def onPress(self, key):
        if self.idleThread != None:
            self.idleThread.theTimer = 0
            self.idleThread.markDirty == False

        return self.running

    def onRelease(self, key):
        if self.idleThread != None:
            self.idleThread.theTimer = 0
            self.idleThread.markDirty == False

        return self.running


class MouseIdleSensorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = False
        self.idleThread = None

    def run(self):
        self.running = True
        with mouse.Listener(
                on_move=self.onMove,
                on_click=self.onClick,
                on_scroll=self.onScroll) as listener:
            listener.join()

    def onMove(self, x, y):
        if self.idleThread != None:
            self.idleThread.theTimer = 0
            self.idleThread.markDirty == False

        return self.running

    def onClick(self, x, y, button, pressed):
        if self.idleThread != None:
            self.idleThread.theTimer = 0
            self.idleThread.markDirty == False

        return self.running

    def onScroll(self, x, y, dx, dy):
        if self.idleThread != None:
            self.idleThread.theTimer = 0
            self.idleThread.markDirty == False

        return self.running


class IdleSensorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.keyboardThread = None
        self.mouseThread = None
        self.theTimer = 0
        self.targetTime = 10
        self.sensitivity = 1
        self.markDirty = False

    def run(self):
        if self.keyboardThread == None or self.mouseThread == None:
            return

        while self.keyboardThread.running == True and self.mouseThread.running == True:
            self.theTimer += self.sensitivity
            time.sleep(self.sensitivity)

            if self.theTimer >= int(self.targetTime) and self.markDirty == False:
                print("shutdown now")
                os.system('shutdown -s')
                self.markDirty = True


class IdleSensor:
    def __init__(self):
        self.keyboardThread = None
        self.mouseThread = None
        self.idleThread = None
        self.targetTime = 2 * 60

    def startService(self):
        self.keyboardThread = KeyboardIdleSensorThread()
        self.mouseThread = MouseIdleSensorThread()
        self.idleThread = IdleSensorThread()

        self.idleThread.keyboardThread = self.keyboardThread
        self.idleThread.mouseThread = self.mouseThread
        self.keyboardThread.idleThread = self.idleThread
        self.mouseThread.idleThread = self.idleThread
        self.idleThread.targetTime = self.targetTime

        self.keyboardThread.start()
        self.mouseThread.start()
        self.idleThread.start()

    def stopService(self):
        if self.keyboardThread != None:
            self.keyboardThread.running = False

        if self.mouseThread != None:
            self.mouseThread.running = False
