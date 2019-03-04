#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskHufuAuthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskHufuAuthQueryResponse, self).__init__()
        self._serial = None
        self._uid = None
        self._user = None

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskHufuAuthQueryResponse, self).parse_response_content(response_content)
        if 'serial' in response:
            self.serial = response['serial']
        if 'uid' in response:
            self.uid = response['uid']
        if 'user' in response:
            self.user = response['user']
