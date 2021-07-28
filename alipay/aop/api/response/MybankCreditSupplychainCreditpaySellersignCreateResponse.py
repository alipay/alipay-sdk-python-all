#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainCreditpaySellersignCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCreditpaySellersignCreateResponse, self).__init__()
        self._ar_no = None
        self._fail_reason = None
        self._ip_id = None
        self._ip_role_id = None
        self._retry = None
        self._sign_result = None
        self._trace_id = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def sign_result(self):
        return self._sign_result

    @sign_result.setter
    def sign_result(self, value):
        self._sign_result = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCreditpaySellersignCreateResponse, self).parse_response_content(response_content)
        if 'ar_no' in response:
            self.ar_no = response['ar_no']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'ip_id' in response:
            self.ip_id = response['ip_id']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'retry' in response:
            self.retry = response['retry']
        if 'sign_result' in response:
            self.sign_result = response['sign_result']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
