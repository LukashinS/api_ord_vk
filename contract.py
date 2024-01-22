from core import BaseMethods


class Contract(BaseMethods):
    """Договоры"""
    def __init__(self, *args):
        super().__init__(*args)

        self.path = "v1/contract"
