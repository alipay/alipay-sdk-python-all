#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntProdpaasProductDeliveryCompleteCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasProductDeliveryCompleteCallbackResponse, self).__init__()
        self._flag = None

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        self._flag = value

    def parse_response_content(self, response_content):
        response = super(AntProdpaasProductDeliveryCompleteCallbackResponse, self).parse_response_content(response_content)
        if 'flag' in response:
            self.flag = response['flag']
