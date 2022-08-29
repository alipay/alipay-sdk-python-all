#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeGuarletterApplyCheckResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeGuarletterApplyCheckResponse, self).__init__()
        self._apply_no = None
        self._inst_name = None
        self._verified = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def verified(self):
        return self._verified

    @verified.setter
    def verified(self, value):
        self._verified = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeGuarletterApplyCheckResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
        if 'verified' in response:
            self.verified = response['verified']
