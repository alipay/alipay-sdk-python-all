#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncGfsettleprodPoamountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfsettleprodPoamountQueryResponse, self).__init__()
        self._po_invoiced_amount = None
        self._po_invoiced_auth_amount = None
        self._po_settled_amount = None

    @property
    def po_invoiced_amount(self):
        return self._po_invoiced_amount

    @po_invoiced_amount.setter
    def po_invoiced_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._po_invoiced_amount = value
        else:
            self._po_invoiced_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def po_invoiced_auth_amount(self):
        return self._po_invoiced_auth_amount

    @po_invoiced_auth_amount.setter
    def po_invoiced_auth_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._po_invoiced_auth_amount = value
        else:
            self._po_invoiced_auth_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def po_settled_amount(self):
        return self._po_settled_amount

    @po_settled_amount.setter
    def po_settled_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._po_settled_amount = value
        else:
            self._po_settled_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfsettleprodPoamountQueryResponse, self).parse_response_content(response_content)
        if 'po_invoiced_amount' in response:
            self.po_invoiced_amount = response['po_invoiced_amount']
        if 'po_invoiced_auth_amount' in response:
            self.po_invoiced_auth_amount = response['po_invoiced_auth_amount']
        if 'po_settled_amount' in response:
            self.po_settled_amount = response['po_settled_amount']
