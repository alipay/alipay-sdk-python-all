#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainPrepaymentApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainPrepaymentApplyResponse, self).__init__()
        self._prepayment_apply_no = None

    @property
    def prepayment_apply_no(self):
        return self._prepayment_apply_no

    @prepayment_apply_no.setter
    def prepayment_apply_no(self, value):
        self._prepayment_apply_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainPrepaymentApplyResponse, self).parse_response_content(response_content)
        if 'prepayment_apply_no' in response:
            self.prepayment_apply_no = response['prepayment_apply_no']
