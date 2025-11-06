#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpInteopAppauthCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopAppauthCreateResponse, self).__init__()
        self._sub_order_no = None

    @property
    def sub_order_no(self):
        return self._sub_order_no

    @sub_order_no.setter
    def sub_order_no(self, value):
        self._sub_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopAppauthCreateResponse, self).parse_response_content(response_content)
        if 'sub_order_no' in response:
            self.sub_order_no = response['sub_order_no']
