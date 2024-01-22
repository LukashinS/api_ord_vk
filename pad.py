from core import BaseMethods


class Pad(BaseMethods):
    """Площадки"""
    def __init__(self, *args):
        super().__init__(*args)

        self.path = "v1/pad"
