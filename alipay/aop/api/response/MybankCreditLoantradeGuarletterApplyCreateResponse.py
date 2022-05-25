#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeGuarletterApplyCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeGuarletterApplyCreateResponse, self).__init__()
        self._apply_no = None
        self._error_code = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeGuarletterApplyCreateResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'error_code' in response:
            self.error_code = response['error_code']
