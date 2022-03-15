import ui

prev_touch = ui.Touch

def detect_touch_type(touch):
    global prev_touch
    

class touch_panel_view(ui.View):
    def touch_began(self, touch):
        detect_touch_type(touch)
    
    def touch_moved(self, touch):
        pass
    
    def touch_ended(self, touch):
        pass