#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthBusinessConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthBusinessConfirmResponse, self).__init__()
        self._fail_reason = None
        self._out_request_no = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthBusinessConfirmResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
