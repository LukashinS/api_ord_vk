import urllib3
import config

bearer = "Bearer"
TOKEN = config.TOKEN
authorization = f'{bearer} {TOKEN}'
accept = 'application/json'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36"

headers = {
    'Authorization': authorization,
    "Accept": accept,
    # "User-Agent": user_agent
}
data = {'offset': '0', 'limit': '100'}
base_url = "https://api.ord.vk.com"


def get_url(base, *args):
    return '/'.join([base] + list(args))


person_url = get_url(base_url, "v1/person")
contract_url = get_url(base_url, "v1/contract")
creative_url = get_url(base_url, "v1/creative")
pad_url = get_url(base_url, "v1/pad")


def get(url):
    urllib3.disable_warnings()
    response = urllib3.request(
        "GET",
        url=url,
        headers=headers)
    return response


def get_list(value):
    """Получение списка"""

    response = get(value)
    external_ids = response.json().get("external_ids")

    result = list()
    for external_id in external_ids:
        url = get_url(value, external_id)
        response = get(url)
        if response:
            result.append(response.json())

    return result


if __name__ == '__main__':
    person_list = get_list(person_url)
    # contract_list = get_list(contract_url)
    # creative_list = get_list(creative_url)
    # pad_list = get_list(pad_url)
    print("Все!")
