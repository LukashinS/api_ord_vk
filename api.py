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
