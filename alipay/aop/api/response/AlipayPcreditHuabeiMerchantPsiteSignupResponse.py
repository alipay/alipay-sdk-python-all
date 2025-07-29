#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiMerchantPsiteSignupResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiMerchantPsiteSignupResponse, self).__init__()
        self._out_request_no = None
        self._record_id = None
        self._signup_status = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def signup_status(self):
        return self._signup_status

    @signup_status.setter
    def signup_status(self, value):
        self._signup_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiMerchantPsiteSignupResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'record_id' in response:
            self.record_id = response['record_id']
        if 'signup_status' in response:
            self.signup_status = response['signup_status']
