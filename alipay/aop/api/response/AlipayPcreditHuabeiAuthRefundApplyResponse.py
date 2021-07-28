#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthRefundApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthRefundApplyResponse, self).__init__()
        self._auth_opt_id = None
        self._fail_reason = None
        self._out_request_no = None
        self._retry = None

    @property
    def auth_opt_id(self):
        return self._auth_opt_id

    @auth_opt_id.setter
    def auth_opt_id(self, value):
        self._auth_opt_id = value
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
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthRefundApplyResponse, self).parse_response_content(response_content)
        if 'auth_opt_id' in response:
            self.auth_opt_id = response['auth_opt_id']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'retry' in response:
            self.retry = response['retry']
