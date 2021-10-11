#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyAmountGetResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyAmountGetResponse, self).__init__()
        self._reason = None
        self._success = None

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyAmountGetResponse, self).parse_response_content(response_content)
        if 'reason' in response:
            self.reason = response['reason']
        if 'success' in response:
            self.success = response['success']
