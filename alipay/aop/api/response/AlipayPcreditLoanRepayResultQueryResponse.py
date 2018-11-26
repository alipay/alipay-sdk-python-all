#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanRepayResultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanRepayResultQueryResponse, self).__init__()
        self._reject_code = None
        self._reject_message = None
        self._repay_status = None

    @property
    def reject_code(self):
        return self._reject_code

    @reject_code.setter
    def reject_code(self, value):
        self._reject_code = value
    @property
    def reject_message(self):
        return self._reject_message

    @reject_message.setter
    def reject_message(self, value):
        self._reject_message = value
    @property
    def repay_status(self):
        return self._repay_status

    @repay_status.setter
    def repay_status(self, value):
        self._repay_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanRepayResultQueryResponse, self).parse_response_content(response_content)
        if 'reject_code' in response:
            self.reject_code = response['reject_code']
        if 'reject_message' in response:
            self.reject_message = response['reject_message']
        if 'repay_status' in response:
            self.repay_status = response['repay_status']
