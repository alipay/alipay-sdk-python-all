#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftBlessGoodwillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftBlessGoodwillQueryResponse, self).__init__()
        self._goodwill_balance = None

    @property
    def goodwill_balance(self):
        return self._goodwill_balance

    @goodwill_balance.setter
    def goodwill_balance(self, value):
        self._goodwill_balance = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftBlessGoodwillQueryResponse, self).parse_response_content(response_content)
        if 'goodwill_balance' in response:
            self.goodwill_balance = response['goodwill_balance']
