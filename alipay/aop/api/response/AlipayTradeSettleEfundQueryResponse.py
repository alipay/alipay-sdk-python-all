#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSettleEfundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSettleEfundQueryResponse, self).__init__()
        self._freeze_amount = None

    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSettleEfundQueryResponse, self).parse_response_content(response_content)
        if 'freeze_amount' in response:
            self.freeze_amount = response['freeze_amount']
