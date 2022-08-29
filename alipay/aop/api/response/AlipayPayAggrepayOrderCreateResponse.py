#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAggrepayOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAggrepayOrderCreateResponse, self).__init__()
        self._pay_data = None

    @property
    def pay_data(self):
        return self._pay_data

    @pay_data.setter
    def pay_data(self, value):
        self._pay_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAggrepayOrderCreateResponse, self).parse_response_content(response_content)
        if 'pay_data' in response:
            self.pay_data = response['pay_data']
