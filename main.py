import urllib3
import config

BASE_URL = config.BASE_URL
TOKEN = config.TOKEN

bearer = "Bearer"
authorization = f'{bearer} {TOKEN}'
accept = 'application/json'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36"

headers = {
    'Authorization': authorization,
    "Accept": accept,
    # "User-Agent": user_agent
}
data = {'offset': '0', 'limit': '100'}


def get_url(base, *args):
    return '/'.join([base] + list(args))


person_url = get_url(BASE_URL, "v1/person")
contract_url = get_url(BASE_URL, "v1/contract")
creative_url = get_url(BASE_URL, "v1/creative")
pad_url = get_url(BASE_URL, "v1/pad")
statistics_url = get_url(BASE_URL, "v1/statistics/list")


def get(url):
    urllib3.disable_warnings()
    response = urllib3.request(
        "GET",
        url=url,
        headers=headers)
    return response


def get_list(value):
    """Получение списка
       Контрагенты/Договоры/Креативы/Площадки"""

    response = get(value)
    external_ids = response.json().get("external_ids")

    result = list()
    for external_id in external_ids:
        url = get_url(value, external_id)
        response = get(url)
        if response:
            result.append(response.json())

    return result


def get_statistics_list():
    """Получение списка Статистики"""

    response = get(statistics_url)
    items = response.json().get("items")

    return items


if __name__ == '__main__':
    print(f"Включен режим - {'PROD' if config.PROD else 'DEV'}")

    # person_list = get_list(person_url)
    # print(person_list)
    #
    # contract_list = get_list(contract_url)
    # print(contract_list)
    #
    # creative_list = get_list(creative_url)
    # print(creative_list)
    #
    # pad_list = get_list(pad_url)
    # print(pad_list)

    statistics_list = get_statistics_list()
    print(statistics_list)

    print("Все!")
