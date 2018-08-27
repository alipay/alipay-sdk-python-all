#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradePartnerPaymentApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePartnerPaymentApplyResponse, self).__init__()
        self._in_apply_no = None

    @property
    def in_apply_no(self):
        return self._in_apply_no

    @in_apply_no.setter
    def in_apply_no(self, value):
        self._in_apply_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePartnerPaymentApplyResponse, self).parse_response_content(response_content)
        if 'in_apply_no' in response:
            self.in_apply_no = response['in_apply_no']
