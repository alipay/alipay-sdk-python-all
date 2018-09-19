#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoPointReceiveQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoPointReceiveQueryResponse, self).__init__()
        self._save_amount = None

    @property
    def save_amount(self):
        return self._save_amount

    @save_amount.setter
    def save_amount(self, value):
        self._save_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoPointReceiveQueryResponse, self).parse_response_content(response_content)
        if 'save_amount' in response:
            self.save_amount = response['save_amount']
