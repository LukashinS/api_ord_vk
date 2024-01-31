from core import BaseMethods
from tabs.contract import Contract
from typing import List
from datetime import datetime
from helpers import sha256sum


class Creative(BaseMethods):
    """Креативы"""
    def __init__(self, *args):
        super().__init__(*args)

        self.path = "v1/creative"
        self.path_v2 = "v2/creative"

    def add_creative(self, name: str, brand: str, category: str, description: str, contract_name: str, okveds: List[str],
                     targeting: str, form: str, pay_type: str, texts: List[str],
                     target_urls: List[str] = [], flags: List[str] = [], file_name: str = None):
        """Создать креатив
        :param name: Название
        :param brand: Бренд
        :param category: Категория
        :param description: Описание
        :param contract_name: Изначальный договор
        :param okveds: Коды ОКВЭД (один или несколько)
        :param targeting: Целевая аудитория
        :param target_urls: Ссылки на внешние ресурсы
        :param form: Тип креатива (text_graphic_block: Текстово-графический блок)
        :param pay_type: Тип рекламной кампании (cpm: Показ, cpc: Клик)
        :param file_name: Имя файла
        :param texts: Текстовые данные креатива
        """
        params = dict(
            name=name,
            brand=brand,
            category=category,
            description=description,
            okveds=okveds,
            targeting=targeting,
            form=form,
            pay_type=pay_type,
            texts=texts,
            target_urls=target_urls,
            flags=flags
        )
        contract = Contract()
        contract_lst = contract.search_contracts_by_comment(contract_name)
        contract_external_id = contract_lst[0]['external_id']
        params['contract_external_id'] = contract_external_id
        if file_name:
            params['media_external_ids'] = [sha256sum(file_name)]
        else:
            params['media_external_ids'] = []

        external_id = str(datetime.now().timestamp()).replace(".", "_")
        url = self.get_url(self.path_v2, external_id)
        response = self.api_client.put(url, params)

        return response.json()
