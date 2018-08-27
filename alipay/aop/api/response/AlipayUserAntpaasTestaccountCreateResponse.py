#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAntpaasTestaccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntpaasTestaccountCreateResponse, self).__init__()
        self._account_level = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._havana_id = None
        self._logon_id = None
        self._logon_type = None
        self._message = None
        self._payment_password = None
        self._query_password = None
        self._success = None
        self._user_id = None
        self._user_status = None
        self._user_type = None

    @property
    def account_level(self):
        return self._account_level

    @account_level.setter
    def account_level(self, value):
        self._account_level = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def logon_type(self):
        return self._logon_type

    @logon_type.setter
    def logon_type(self, value):
        self._logon_type = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def payment_password(self):
        return self._payment_password

    @payment_password.setter
    def payment_password(self, value):
        self._payment_password = value
    @property
    def query_password(self):
        return self._query_password

    @query_password.setter
    def query_password(self, value):
        self._query_password = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntpaasTestaccountCreateResponse, self).parse_response_content(response_content)
        if 'account_level' in response:
            self.account_level = response['account_level']
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'havana_id' in response:
            self.havana_id = response['havana_id']
        if 'logon_id' in response:
            self.logon_id = response['logon_id']
        if 'logon_type' in response:
            self.logon_type = response['logon_type']
        if 'message' in response:
            self.message = response['message']
        if 'payment_password' in response:
            self.payment_password = response['payment_password']
        if 'query_password' in response:
            self.query_password = response['query_password']
        if 'success' in response:
            self.success = response['success']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_status' in response:
            self.user_status = response['user_status']
        if 'user_type' in response:
            self.user_type = response['user_type']
