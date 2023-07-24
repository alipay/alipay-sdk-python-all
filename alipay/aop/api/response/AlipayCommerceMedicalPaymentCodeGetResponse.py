#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPaymentCodeGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPaymentCodeGetResponse, self).__init__()
        self._login_name = None
        self._payment_code = None

    @property
    def login_name(self):
        return self._login_name

    @login_name.setter
    def login_name(self, value):
        self._login_name = value
    @property
    def payment_code(self):
        return self._payment_code

    @payment_code.setter
    def payment_code(self, value):
        self._payment_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPaymentCodeGetResponse, self).parse_response_content(response_content)
        if 'login_name' in response:
            self.login_name = response['login_name']
        if 'payment_code' in response:
            self.payment_code = response['payment_code']
