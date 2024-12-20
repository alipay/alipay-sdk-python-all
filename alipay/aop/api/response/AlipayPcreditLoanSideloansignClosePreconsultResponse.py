#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanSideloansignClosePreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloansignClosePreconsultResponse, self).__init__()
        self._check_status = None
        self._fail_reanson_message = None
        self._fail_reason_code = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def check_status(self):
        return self._check_status

    @check_status.setter
    def check_status(self, value):
        self._check_status = value
    @property
    def fail_reanson_message(self):
        return self._fail_reanson_message

    @fail_reanson_message.setter
    def fail_reanson_message(self, value):
        self._fail_reanson_message = value
    @property
    def fail_reason_code(self):
        return self._fail_reason_code

    @fail_reason_code.setter
    def fail_reason_code(self, value):
        self._fail_reason_code = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_sub_code(self):
        return self._return_sub_code

    @return_sub_code.setter
    def return_sub_code(self, value):
        self._return_sub_code = value
    @property
    def return_sub_message(self):
        return self._return_sub_message

    @return_sub_message.setter
    def return_sub_message(self, value):
        self._return_sub_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloansignClosePreconsultResponse, self).parse_response_content(response_content)
        if 'check_status' in response:
            self.check_status = response['check_status']
        if 'fail_reanson_message' in response:
            self.fail_reanson_message = response['fail_reanson_message']
        if 'fail_reason_code' in response:
            self.fail_reason_code = response['fail_reason_code']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
