#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflinePaysaasOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflinePaysaasOrderCreateResponse, self).__init__()
        self._isv_order_no = None

    @property
    def isv_order_no(self):
        return self._isv_order_no

    @isv_order_no.setter
    def isv_order_no(self, value):
        self._isv_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflinePaysaasOrderCreateResponse, self).parse_response_content(response_content)
        if 'isv_order_no' in response:
            self.isv_order_no = response['isv_order_no']
