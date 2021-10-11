#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankBanktradeinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankBanktradeinfoQueryResponse, self).__init__()
        self._bank_card_type = None
        self._bank_inst_id = None

    @property
    def bank_card_type(self):
        return self._bank_card_type

    @bank_card_type.setter
    def bank_card_type(self, value):
        self._bank_card_type = value
    @property
    def bank_inst_id(self):
        return self._bank_inst_id

    @bank_inst_id.setter
    def bank_inst_id(self, value):
        self._bank_inst_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankBanktradeinfoQueryResponse, self).parse_response_content(response_content)
        if 'bank_card_type' in response:
            self.bank_card_type = response['bank_card_type']
        if 'bank_inst_id' in response:
            self.bank_inst_id = response['bank_inst_id']
