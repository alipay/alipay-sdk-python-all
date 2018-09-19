#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemDiagnoseDetail import ItemDiagnoseDetail


class KoubeiMarketingDataDishdiagnoseBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataDishdiagnoseBatchqueryResponse, self).__init__()
        self._item_diagnose_list = None
        self._total = None

    @property
    def item_diagnose_list(self):
        return self._item_diagnose_list

    @item_diagnose_list.setter
    def item_diagnose_list(self, value):
        if isinstance(value, list):
            self._item_diagnose_list = list()
            for i in value:
                if isinstance(i, ItemDiagnoseDetail):
                    self._item_diagnose_list.append(i)
                else:
                    self._item_diagnose_list.append(ItemDiagnoseDetail.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataDishdiagnoseBatchqueryResponse, self).parse_response_content(response_content)
        if 'item_diagnose_list' in response:
            self.item_diagnose_list = response['item_diagnose_list']
        if 'total' in response:
            self.total = response['total']
