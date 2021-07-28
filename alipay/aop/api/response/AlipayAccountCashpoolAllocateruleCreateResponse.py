#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountCashpoolAllocateruleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountCashpoolAllocateruleCreateResponse, self).__init__()
        self._rule_id = None

    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountCashpoolAllocateruleCreateResponse, self).parse_response_content(response_content)
        if 'rule_id' in response:
            self.rule_id = response['rule_id']
