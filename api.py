import urllib3


class ApiClient:
    """Класс для работы с GET/POST запросами"""

    def __init__(self, token):
        self.TOKEN = token
        self.bearer = "Bearer"
        self.authorization = f'{self.bearer} {self.TOKEN}'
        self.accept = 'application/json'
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36"
        self.headers = {
            'Authorization': self.authorization,
            "Accept": self.accept,
            # "User-Agent": self.user_agent
        }
        self.data = {'offset': '0', 'limit': '100'}

    def get(self, url):
        urllib3.disable_warnings()
        response = urllib3.request(
            "GET",
            url=url,
            headers=self.headers)
        return response


class BaseMethods:
    def __init__(self, base_url, token):
        self.api_client = ApiClient(token)
        self.BASE_URL = base_url
        self.person_url = "v1/person"
        self.contract_url = "v1/contract"
        self.creative_url = "v1/creative"
        self.pad_url = "v1/pad"
        self.statistics_url = "v1/statistics/list"

    def get_url(self, *args):
        return '/'.join([self.BASE_URL] + list(args))

    def get_list(self, value):
        """Получение списка
       Контрагенты/Договоры/Креативы/Площадки"""

        url = self.get_url(value)
        response = self.api_client.get(url)
        external_ids = response.json().get("external_ids")
        result = list()
        for external_id in external_ids:
            url = self.get_url(value, external_id)
            response = self.api_client.get(url)
            if response:
                result.append(response.json())
        return result

    def get_statistics_list(self):
        """Получение списка Статистики"""

        url = self.get_url(self.statistics_url)
        response = self.api_client.get(url)
        items = response.json().get("items")
        return items
