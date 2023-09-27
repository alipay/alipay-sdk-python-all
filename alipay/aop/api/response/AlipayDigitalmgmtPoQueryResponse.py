#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PurchaseOrderOutDTO import PurchaseOrderOutDTO


class AlipayDigitalmgmtPoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtPoQueryResponse, self).__init__()
        self._purchase_order_list = None

    @property
    def purchase_order_list(self):
        return self._purchase_order_list

    @purchase_order_list.setter
    def purchase_order_list(self, value):
        if isinstance(value, list):
            self._purchase_order_list = list()
            for i in value:
                if isinstance(i, PurchaseOrderOutDTO):
                    self._purchase_order_list.append(i)
                else:
                    self._purchase_order_list.append(PurchaseOrderOutDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtPoQueryResponse, self).parse_response_content(response_content)
        if 'purchase_order_list' in response:
            self.purchase_order_list = response['purchase_order_list']
