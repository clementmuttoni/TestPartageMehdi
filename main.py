from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from random import randint


class JeuPerles(Widget):
	perleVoyA = ObjectProperty(None)
	perleVoyB = ObjectProperty(None)
	
	def update(self,dt):
		print("rien pour le moment")
   

class Perle(Widget):
		
	def on_touch_move(self, touch):
			self.center = touch.pos
    
   

class PerlesApp(App):
	
    def build(self):
		jeuP = JeuPerles()
		#Clock.schedule_interval(jeuP.update, 1.0/60.0
		return jeuP


if __name__ == '__main__':
    PerlesApp().run()
