#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxUserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxUserinfoQueryResponse, self).__init__()
        self._eligible = None
        self._eligible_msg = None
        self._logon_id = None
        self._user_id = None
        self._user_name = None

    @property
    def eligible(self):
        return self._eligible

    @eligible.setter
    def eligible(self, value):
        self._eligible = value
    @property
    def eligible_msg(self):
        return self._eligible_msg

    @eligible_msg.setter
    def eligible_msg(self, value):
        self._eligible_msg = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxUserinfoQueryResponse, self).parse_response_content(response_content)
        if 'eligible' in response:
            self.eligible = response['eligible']
        if 'eligible_msg' in response:
            self.eligible_msg = response['eligible_msg']
        if 'logon_id' in response:
            self.logon_id = response['logon_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
