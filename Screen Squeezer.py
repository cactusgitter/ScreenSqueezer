# Screen Squeezer is an app that will let the user set a screen ratio
# and keep all elements within the app to that ratio.

import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

# ScreenSqueezerApp is the primary class that instantiates a window.
# All other widgets fall under this widget.
class ScreenSqueezerApp(App):		
	def build(self): # Runs every time an instance is created
		frame_res = [1960,1080] #The starting resolution
		
		def resizeLayout(layout, newx, newy):
			nonlocal frame_res
			frame_res = [newx, newy]
			if newx == newy:
				layout.size_hint = [1,1]
			else:
				frame_ratio = newx / newy # The frame ratio given by width / height
				frame_inverse_ratio = newy / newx # The frame ratio given by height / width
				window_ratio = Window.width / Window.height # The window ratio given by width / height
				if frame_ratio < window_ratio: #If the window width is wider than the frame width
					layout.size_hint = [None,1] # Specific width, maximum height
					layout.width = Window.height * frame_ratio
				if frame_ratio > window_ratio: #If the window width is smaller than the frame width
					layout.size_hint = [1,None] # maximum width, specific height
					layout.height = Window.width * frame_inverse_ratio
					
		primaryLayout = BoxLayout(orientation='vertical', 
								width = Window.width * 0.7, 
								height = Window.height * 0.5,
								pos_hint = {'center_x':0.5,'center_y':0.5}, #Center the layout within the parent layout or window
								size_hint = [1,1])
		
		btn = Button(text = "1960 x 1080", size_hint_y = 1, size_hint_x = 1)
		btn.bind(on_press = lambda x: resizeLayout(primaryLayout, 1960, 1080))
		primaryLayout.add_widget(btn)
		
		btn = Button(text = "4:3", size_hint_y = 1, size_hint_x = 1)
		btn.bind(on_press = lambda x: resizeLayout(primaryLayout, 5, 3))
		primaryLayout.add_widget(btn)
		
		btn = Button(text = "3:4", size_hint_y = 1, size_hint_x = 1)
		btn.bind(on_press = lambda x: resizeLayout(primaryLayout, 3, 4))
		primaryLayout.add_widget(btn)		
		
		Window.bind(on_resize = lambda self, x, y: resizeLayout(primaryLayout, frame_res[0], frame_res[1]))
		resizeLayout(primaryLayout, frame_res[0], frame_res[1]) #Sets the initial resolution, otherwise defaults to size_hint = 1,1
		
		return primaryLayout
		
ScreenSqueezerApp().run() #Instantiates the app

# Just leave this stuff here at the bottom
def main(args):
	return 0
	
# Just leave this stuff here at the bottom
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
