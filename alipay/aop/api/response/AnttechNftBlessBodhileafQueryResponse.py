#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftBlessBodhileafQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftBlessBodhileafQueryResponse, self).__init__()
        self._bodhi_leaf_balance = None

    @property
    def bodhi_leaf_balance(self):
        return self._bodhi_leaf_balance

    @bodhi_leaf_balance.setter
    def bodhi_leaf_balance(self, value):
        self._bodhi_leaf_balance = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftBlessBodhileafQueryResponse, self).parse_response_content(response_content)
        if 'bodhi_leaf_balance' in response:
            self.bodhi_leaf_balance = response['bodhi_leaf_balance']
