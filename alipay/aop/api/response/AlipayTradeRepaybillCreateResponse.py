#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRepaybillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRepaybillCreateResponse, self).__init__()
        self._bill_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRepaybillCreateResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
