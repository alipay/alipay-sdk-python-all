#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpInteopOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopOrderCreateResponse, self).__init__()
        self._inteop_order_no = None

    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopOrderCreateResponse, self).parse_response_content(response_content)
        if 'inteop_order_no' in response:
            self.inteop_order_no = response['inteop_order_no']
