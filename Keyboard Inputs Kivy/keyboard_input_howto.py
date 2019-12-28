class wdgt(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        with self.canvas:
            self.player = Rectangle(source='', pos=(0,0), size=(100,100))

        self.keysPressed = set()

        Clock.schedule_interval(self.move_step, 0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_up(self, keyboard, keycode):
        if keycode[1] in self.keysPressed:
            self.keysPressed.remove(keycode[1])

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(keycode[1])

    def move_step(self,dt):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        step_size = 200 * dt

        if 'up' in self.keysPressed:
            currenty += step_size
        if 'down' in self.keysPressed:
            currenty -= step_size
        if 'right' in self.keysPressed:
            currentx += step_size
        if 'left' in self.keysPressed:
            currentx -= step_size

        self.player.pos = (currentx, currenty)