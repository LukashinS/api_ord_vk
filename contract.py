from core import BaseMethods


class Contract(BaseMethods):
    """Договоры"""
    def __init__(self, *args):
        super().__init__(*args)

        self.path = "v1/contract"

    def search_contracts_by_comment(self, comment):
        contract_lst = self.get_list()
        return list(filter(lambda x: x["comment"] == comment, contract_lst))
