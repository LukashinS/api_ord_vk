from core import BaseMethods


class Person(BaseMethods):
    """Контрагенты"""
    def __init__(self, *args):
        super().__init__(*args)

        self.path = "v1/person"
