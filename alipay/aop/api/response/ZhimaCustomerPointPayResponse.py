#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerPointPayResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerPointPayResponse, self).__init__()
        self._pay_finished = None

    @property
    def pay_finished(self):
        return self._pay_finished

    @pay_finished.setter
    def pay_finished(self, value):
        self._pay_finished = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerPointPayResponse, self).parse_response_content(response_content)
        if 'pay_finished' in response:
            self.pay_finished = response['pay_finished']
