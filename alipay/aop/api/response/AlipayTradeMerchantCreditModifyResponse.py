#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeMerchantCreditModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeMerchantCreditModifyResponse, self).__init__()
        self._current_credit_quota = None
        self._granted_credit_quota = None
        self._out_request_no = None

    @property
    def current_credit_quota(self):
        return self._current_credit_quota

    @current_credit_quota.setter
    def current_credit_quota(self, value):
        self._current_credit_quota = value
    @property
    def granted_credit_quota(self):
        return self._granted_credit_quota

    @granted_credit_quota.setter
    def granted_credit_quota(self, value):
        self._granted_credit_quota = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeMerchantCreditModifyResponse, self).parse_response_content(response_content)
        if 'current_credit_quota' in response:
            self.current_credit_quota = response['current_credit_quota']
        if 'granted_credit_quota' in response:
            self.granted_credit_quota = response['granted_credit_quota']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
