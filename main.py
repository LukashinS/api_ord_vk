import config
from tabs.person import Person
from tabs.contract import Contract
from tabs.creative import Creative
from tabs.pad import Pad
from tabs.statistics import Statistics

if __name__ == '__main__':
    print(f"Включен режим - {'PROD' if config.PROD else 'DEV'}")

    # person = Person()
    # person_list = person.get_list()
    # print(person_list)
    #
    contract = Contract()
    contract_list = contract.get_list()
    print(contract_list)

    creative = Creative()
    creative_list = creative.get_list()
    cr_1 = {}
    cr_response = creative.add_creative(contract_name="", file_name="", **cr_1)
    print(cr_response['erid'])

    # pad = Pad()
    # pad_list = pad.get_list()
    # print(pad_list)
    #
    # statistics = Statistics()
    # statistics_list = statistics.get_list()
    # print(statistics_list)

    print("Все!")
