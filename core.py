import helpers
from api import ApiClient
import config

BASE_URL = config.BASE_URL


class BaseMethods:
    def __init__(self, path=""):
        self.api_client = ApiClient()
        self.base_url = BASE_URL
        self.path = path

    def get_url(self, *args):
        """Генерация url'а запроса"""

        return '/'.join([self.base_url] + list(args))

    def get_list(self):
        """Получение списка
       Контрагенты/Договоры/Креативы/Площадки"""

        url = self.get_url(self.path)
        response = self.api_client.get(url)
        external_ids = response.json().get("external_ids")
        result = list()
        for external_id in external_ids:
            url = self.get_url(self.path, external_id)
            response = self.api_client.get(url)
            if response:
                r_json = response.json()
                r_json['external_id'] = external_id
                result.append(r_json)
        return result

    def record_list_to_xls(self, path_to_json="list.json", path_to_xls="list.xlsx"):
        """Запись списка в Excel файл"""

        result = self.get_list()
        helpers.save_to_json(result, path_to_json)
        helpers.save_json_to_xls(path_to_json, path_to_xls)
