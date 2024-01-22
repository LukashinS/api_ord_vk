import config
from api import BaseMethods

BASE_URL = config.BASE_URL
TOKEN = config.TOKEN


if __name__ == '__main__':

    main = BaseMethods(config.BASE_URL, config.TOKEN)

    print(f"Включен режим - {'PROD' if config.PROD else 'DEV'}")

    person_list = main.get_list(main.person_url)
    print(person_list)

    contract_list = main.get_list(main.contract_url)
    print(contract_list)

    creative_list = main.get_list(main.creative_url)
    print(creative_list)

    pad_list = main.get_list(main.pad_url)
    print(pad_list)

    statistics_list = main.get_statistics_list()
    print(statistics_list)

    print("Все!")
