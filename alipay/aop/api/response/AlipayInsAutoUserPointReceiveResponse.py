#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoUserPointReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoUserPointReceiveResponse, self).__init__()
        self._save_amount = None

    @property
    def save_amount(self):
        return self._save_amount

    @save_amount.setter
    def save_amount(self, value):
        self._save_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoUserPointReceiveResponse, self).parse_response_content(response_content)
        if 'save_amount' in response:
            self.save_amount = response['save_amount']
