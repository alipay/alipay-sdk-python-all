#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradePayArSignResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayArSignResponse, self).__init__()
        self._error_code = None
        self._guide_param = None
        self._refuse_code = None
        self._signed_ar = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def guide_param(self):
        return self._guide_param

    @guide_param.setter
    def guide_param(self, value):
        self._guide_param = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def signed_ar(self):
        return self._signed_ar

    @signed_ar.setter
    def signed_ar(self, value):
        self._signed_ar = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePayArSignResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'guide_param' in response:
            self.guide_param = response['guide_param']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'signed_ar' in response:
            self.signed_ar = response['signed_ar']
        if 'success' in response:
            self.success = response['success']
