import urllib3
import config

TOKEN = config.TOKEN


class ApiClient:
    """Класс для работы с GET/POST запросами"""

    def __init__(self):
        self.TOKEN = TOKEN
        self.authorization = f'Bearer {self.TOKEN}'
        self.accept = 'application/json'
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36"
        self.headers = {
            'Authorization': self.authorization,
            "Accept": self.accept,
            # "User-Agent": self.user_agent
        }
        self.data = {'offset': '0', 'limit': '100'}

    def get(self, url):
        """GET - Чтение"""

        urllib3.disable_warnings()
        response = urllib3.request(
            "GET",
            url=url,
            headers=self.headers)
        return response

    def put(self, url, params):
        """PUT - Запись"""
        urllib3.disable_warnings()
        headers = {"Content-Type": self.accept}
        headers.update(**self.headers)
        response = urllib3.request(
            "PUT",
            url=url,
            headers=headers,
            json=params)
        return response
