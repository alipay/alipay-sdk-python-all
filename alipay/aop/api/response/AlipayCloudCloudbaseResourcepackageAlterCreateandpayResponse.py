#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseResourcepackageAlterCreateandpayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageAlterCreateandpayResponse, self).__init__()
        self._order_no = None
        self._result = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageAlterCreateandpayResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'result' in response:
            self.result = response['result']
