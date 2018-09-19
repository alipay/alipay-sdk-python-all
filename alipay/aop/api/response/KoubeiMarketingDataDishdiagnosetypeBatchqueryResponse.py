#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemDiagnoseType import ItemDiagnoseType


class KoubeiMarketingDataDishdiagnosetypeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataDishdiagnosetypeBatchqueryResponse, self).__init__()
        self._item_diagnose_type_list = None

    @property
    def item_diagnose_type_list(self):
        return self._item_diagnose_type_list

    @item_diagnose_type_list.setter
    def item_diagnose_type_list(self, value):
        if isinstance(value, list):
            self._item_diagnose_type_list = list()
            for i in value:
                if isinstance(i, ItemDiagnoseType):
                    self._item_diagnose_type_list.append(i)
                else:
                    self._item_diagnose_type_list.append(ItemDiagnoseType.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataDishdiagnosetypeBatchqueryResponse, self).parse_response_content(response_content)
        if 'item_diagnose_type_list' in response:
            self.item_diagnose_type_list = response['item_diagnose_type_list']
