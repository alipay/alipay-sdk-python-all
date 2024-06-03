#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCardGenerateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCardGenerateCreateResponse, self).__init__()
        self._fund_card_generate_no = None

    @property
    def fund_card_generate_no(self):
        return self._fund_card_generate_no

    @fund_card_generate_no.setter
    def fund_card_generate_no(self, value):
        self._fund_card_generate_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCardGenerateCreateResponse, self).parse_response_content(response_content)
        if 'fund_card_generate_no' in response:
            self.fund_card_generate_no = response['fund_card_generate_no']
