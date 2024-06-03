#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionAccountModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionAccountModifyResponse, self).__init__()
        self._account_no = None
        self._account_status = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionAccountModifyResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'account_status' in response:
            self.account_status = response['account_status']
