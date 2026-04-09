#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceBankaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceBankaccountQueryResponse, self).__init__()
        self._bank_name = None
        self._fail_reason = None
        self._merchant_name = None
        self._merchant_pid = None
        self._status = None

    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceBankaccountQueryResponse, self).parse_response_content(response_content)
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'status' in response:
            self.status = response['status']
