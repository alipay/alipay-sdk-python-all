#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeGuarletterApplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeGuarletterApplyQueryResponse, self).__init__()
        self._accept_result = None
        self._reject_reason = None

    @property
    def accept_result(self):
        return self._accept_result

    @accept_result.setter
    def accept_result(self, value):
        self._accept_result = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeGuarletterApplyQueryResponse, self).parse_response_content(response_content)
        if 'accept_result' in response:
            self.accept_result = response['accept_result']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
