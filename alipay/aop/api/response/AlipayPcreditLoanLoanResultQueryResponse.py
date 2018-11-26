#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanLoanResultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanLoanResultQueryResponse, self).__init__()
        self._apply_status = None
        self._reject_code = None
        self._reject_message = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanLoanResultQueryResponse, self).parse_response_content(response_content)
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
        if 'reject_code' in response:
            self.reject_code = response['reject_code']
        if 'reject_message' in response:
            self.reject_message = response['reject_message']
