#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileShakeUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileShakeUserQueryResponse, self).__init__()
        self._bizdata = None
        self._logon_id = None
        self._pass_id = None
        self._user_id = None

    @property
    def bizdata(self):
        return self._bizdata

    @bizdata.setter
    def bizdata(self, value):
        self._bizdata = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def pass_id(self):
        return self._pass_id

    @pass_id.setter
    def pass_id(self, value):
        self._pass_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileShakeUserQueryResponse, self).parse_response_content(response_content)
        if 'bizdata' in response:
            self.bizdata = response['bizdata']
        if 'logon_id' in response:
            self.logon_id = response['logon_id']
        if 'pass_id' in response:
            self.pass_id = response['pass_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
