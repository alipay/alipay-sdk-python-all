#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeIndfinsolCreditQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeIndfinsolCreditQueryResponse, self).__init__()
        self._bank_card_number = None
        self._inst_id = None

    @property
    def bank_card_number(self):
        return self._bank_card_number

    @bank_card_number.setter
    def bank_card_number(self, value):
        self._bank_card_number = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeIndfinsolCreditQueryResponse, self).parse_response_content(response_content)
        if 'bank_card_number' in response:
            self.bank_card_number = response['bank_card_number']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
