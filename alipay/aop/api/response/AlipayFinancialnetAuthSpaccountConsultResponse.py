#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthSpaccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthSpaccountConsultResponse, self).__init__()
        self._display_opened_account_logon_id = None
        self._error_code = None
        self._error_message = None
        self._is_success = None
        self._opened_account = None
        self._opened_account_user_id = None

    @property
    def display_opened_account_logon_id(self):
        return self._display_opened_account_logon_id

    @display_opened_account_logon_id.setter
    def display_opened_account_logon_id(self, value):
        self._display_opened_account_logon_id = value
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
    @property
    def opened_account(self):
        return self._opened_account

    @opened_account.setter
    def opened_account(self, value):
        self._opened_account = value
    @property
    def opened_account_user_id(self):
        return self._opened_account_user_id

    @opened_account_user_id.setter
    def opened_account_user_id(self, value):
        self._opened_account_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthSpaccountConsultResponse, self).parse_response_content(response_content)
        if 'display_opened_account_logon_id' in response:
            self.display_opened_account_logon_id = response['display_opened_account_logon_id']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'opened_account' in response:
            self.opened_account = response['opened_account']
        if 'opened_account_user_id' in response:
            self.opened_account_user_id = response['opened_account_user_id']
