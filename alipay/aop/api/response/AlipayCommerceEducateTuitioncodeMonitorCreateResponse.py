#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateTuitioncodeMonitorCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTuitioncodeMonitorCreateResponse, self).__init__()
        self._account_name = None
        self._account_no = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTuitioncodeMonitorCreateResponse, self).parse_response_content(response_content)
        if 'account_name' in response:
            self.account_name = response['account_name']
        if 'account_no' in response:
            self.account_no = response['account_no']
