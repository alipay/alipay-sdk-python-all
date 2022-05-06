#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataBillBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataBillBalanceQueryResponse, self).__init__()
        self._available_amount = None
        self._freeze_amount = None
        self._settle_amount = None
        self._total_amount = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataBillBalanceQueryResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'freeze_amount' in response:
            self.freeze_amount = response['freeze_amount']
        if 'settle_amount' in response:
            self.settle_amount = response['settle_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
