from core import BaseMethods


class Statistics(BaseMethods):
    """Статистика"""
    def __init__(self, *args):
        super().__init__(*args)

        self.path = "v1/statistics/list"

    def get_list(self):
        """Получение списка Статистики"""

        url = self.get_url(self.path)
        response = self.api_client.get(url)
        items = response.json().get("items")
        return items
