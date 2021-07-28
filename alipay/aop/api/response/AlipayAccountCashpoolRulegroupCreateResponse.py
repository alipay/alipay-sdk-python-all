#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountCashpoolRulegroupCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountCashpoolRulegroupCreateResponse, self).__init__()
        self._rule_group_id = None

    @property
    def rule_group_id(self):
        return self._rule_group_id

    @rule_group_id.setter
    def rule_group_id(self, value):
        self._rule_group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountCashpoolRulegroupCreateResponse, self).parse_response_content(response_content)
        if 'rule_group_id' in response:
            self.rule_group_id = response['rule_group_id']
