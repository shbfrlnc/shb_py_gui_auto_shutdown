# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseDialog
###########################################################################

class BaseDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SHB PY GUI Auto Shutdown", pos = wx.DefaultPosition, size = wx.Size( 359,162 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		m_b_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_static_text_shutdown_after = wx.StaticText( self, wx.ID_ANY, u"Shutdown After (Minutes of Idle)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_shutdown_after.Wrap( -1 )

		m_b_sizer.Add( self.m_static_text_shutdown_after, 0, wx.ALL, 5 )

		self.m_spin_ctrl_shutdown_after = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 2, 1440, 2 )
		self.m_spin_ctrl_shutdown_after.SetMinSize( wx.Size( 9999,-1 ) )

		m_b_sizer.Add( self.m_spin_ctrl_shutdown_after, 0, wx.ALL, 5 )

		self.m_button_toggle_idle_sensor = wx.Button( self, wx.ID_ANY, u"Idle Sensor is Enabled", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_toggle_idle_sensor.SetMinSize( wx.Size( 9999,9999 ) )

		m_b_sizer.Add( self.m_button_toggle_idle_sensor, 0, wx.ALL, 5 )


		self.SetSizer( m_b_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


