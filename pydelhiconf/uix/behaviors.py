''' 
Custom Behaviors are defined in this module.
'''
from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import (NumericProperty, StringProperty,
                             ListProperty)
from kivy.graphics import (Rectangle, Color, Ellipse, StencilPop,
                           StencilPush, StencilUnUse, StencilUse)



class TouchRippleBehavior(EventDispatcher):

    __events__ = ('on_released',) 

    ripple_rad = NumericProperty(10)
    ripple_pos = ListProperty([0, 0])
    #141 ,188, 234
    ripple_color = ListProperty((141./256., 188./256., 234./256., 1))
    ripple_duration_in = NumericProperty(.3)
    ripple_duration_out = NumericProperty(.3)
    fade_to_alpha = NumericProperty(.3)
    ripple_scale = NumericProperty(2.0)
    ripple_func_in = StringProperty('out_quad')
    ripple_func_out = StringProperty('in_quad')

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            # self.anim_complete(self, self)
            self.ripple_pos = ripple_pos = (touch.x, touch.y)
            Animation.cancel_all(self, 'ripple_rad', 'ripple_color')
            rc = self.ripple_color
            ripple_rad = self.ripple_rad
            self.ripple_color = [rc[0], rc[1], rc[2], 1.]
            anim = Animation(
                ripple_rad=max(self.width, self.height) * self.ripple_scale, 
                t=self.ripple_func_in,
                ripple_color=[rc[0], rc[1], rc[2], self.fade_to_alpha], 
                duration=self.ripple_duration_in)
            anim.bind(on_complete=self.anim_complete)
            anim.start(self)
            with self.canvas:
                StencilPush()
                Rectangle(size=self.size, pos=self.pos)
                StencilUse()
                self.col_instruction = Color(rgba=self.ripple_color, group='one')
                self.ellipse = Ellipse(size=(ripple_rad, ripple_rad),
                    pos=(ripple_pos[0] - ripple_rad/2., 
                    ripple_pos[1] - ripple_rad/2.),
                    group='one')
                StencilUnUse()
                Rectangle(size=self.size, pos=self.pos)
                StencilPop()
            self.bind(ripple_color=self.set_color, ripple_pos=self.set_ellipse,
                ripple_rad=self.set_ellipse)
        return super(TouchRippleBehavior, self).on_touch_down(touch)

    def set_ellipse(self, instance, value):
        ellipse = self.ellipse
        ripple_pos = self.ripple_pos
        ripple_rad = self.ripple_rad
        ellipse.size = (ripple_rad, ripple_rad)
        ellipse.pos = (ripple_pos[0] - ripple_rad/2., 
            ripple_pos[1] - ripple_rad/2.)

    def set_color(self, instance, value):
        self.col_instruction.rgba = value

    def on_release(self):
        rc = self.ripple_color
        anim = Animation(ripple_color=[rc[0], rc[1], rc[2], 0.], 
            t=self.ripple_func_out, duration=self.ripple_duration_out)
        anim.bind(on_complete=self.anim_completed)
        anim.start(self)

    def anim_complete(self, anim, instance):
        self.ripple_rad = 10
        self.canvas.remove_group('one')

    def on_released(self):
        pass

    def anim_completed(self, anim, instance):
        self.anim_complete(anim, instance)
        self.dispatch('on_released')
