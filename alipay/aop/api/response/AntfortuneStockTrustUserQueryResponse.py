#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneStockTrustUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockTrustUserQueryResponse, self).__init__()
        self._cert_no = None
        self._phone = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockTrustUserQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'phone' in response:
            self.phone = response['phone']
        if 'user_name' in response:
            self.user_name = response['user_name']
