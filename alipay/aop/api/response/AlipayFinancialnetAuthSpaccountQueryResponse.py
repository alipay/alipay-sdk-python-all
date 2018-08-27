#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpAccountInfo import SpAccountInfo


class AlipayFinancialnetAuthSpaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthSpaccountQueryResponse, self).__init__()
        self._account_info = None
        self._error_code = None
        self._error_message = None
        self._is_success = None

    @property
    def account_info(self):
        return self._account_info

    @account_info.setter
    def account_info(self, value):
        if isinstance(value, list):
            self._account_info = list()
            for i in value:
                if isinstance(i, SpAccountInfo):
                    self._account_info.append(i)
                else:
                    self._account_info.append(SpAccountInfo.from_alipay_dict(i))
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthSpaccountQueryResponse, self).parse_response_content(response_content)
        if 'account_info' in response:
            self.account_info = response['account_info']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'is_success' in response:
            self.is_success = response['is_success']
