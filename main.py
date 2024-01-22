import config
from person import Person
from contract import Contract
from creative import Creative
from pad import Pad
from statistics import Statistics


if __name__ == '__main__':

    print(f"Включен режим - {'PROD' if config.PROD else 'DEV'}")

    person = Person()
    person_list = person.get_list()
    print(person_list)

    contract = Contract()
    contract_list = contract.get_list()
    print(contract_list)

    creative = Creative()
    creative_list = creative.get_list()
    print(creative_list)

    pad = Pad()
    pad_list = pad.get_list()
    print(pad_list)

    statistics = Statistics()
    statistics_list = statistics.get_list()
    print(statistics_list)

    print("Все!")
