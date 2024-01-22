from core import BaseMethods


class Creative(BaseMethods):
    """Креативы"""
    def __init__(self, *args):
        super().__init__(*args)

        self.path = "v1/creative"
