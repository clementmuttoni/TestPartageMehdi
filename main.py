# -*-coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from random import randint


class JeuPerles(Widget):
	perleVoyA = ObjectProperty(None)
	perleVoyB = ObjectProperty(None)
	
	
	
		
	
	
	
	#def on_touch_move(self, touch):
	#		self.perleVoyA.center = touch.pos
		
   

class Perle(Widget):
	
	def __init__(self, voy):
		voyelle = voy
		
	def on_touch_move(self, touch):
		#if touch.y > self.height/2:
			self.center = touch.pos
		#if touch.y < self.height/2:
		#	self.perleVoyB.center = touch.pos	
	
	
	

    
   

class PerlesApp(App):
	
    def build(self):
		jeuP = JeuPerles()
		#Clock.schedule_interval(jeuP.update, 1.0/60.0
		return jeuP


if __name__ == '__main__':
    PerlesApp().run()
