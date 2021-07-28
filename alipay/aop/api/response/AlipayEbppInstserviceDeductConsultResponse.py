#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceDeductConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceDeductConsultResponse, self).__init__()
        self._allow_sign = None
        self._error_code = None
        self._extend_field = None
        self._pay_mode = None

    @property
    def allow_sign(self):
        return self._allow_sign

    @allow_sign.setter
    def allow_sign(self, value):
        self._allow_sign = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceDeductConsultResponse, self).parse_response_content(response_content)
        if 'allow_sign' in response:
            self.allow_sign = response['allow_sign']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'pay_mode' in response:
            self.pay_mode = response['pay_mode']
