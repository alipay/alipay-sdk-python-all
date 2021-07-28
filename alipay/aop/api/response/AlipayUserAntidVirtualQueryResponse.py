#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAntidVirtualQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntidVirtualQueryResponse, self).__init__()
        self._ant_id = None
        self._ext_info = None
        self._user_id = None

    @property
    def ant_id(self):
        return self._ant_id

    @ant_id.setter
    def ant_id(self, value):
        self._ant_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntidVirtualQueryResponse, self).parse_response_content(response_content)
        if 'ant_id' in response:
            self.ant_id = response['ant_id']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'user_id' in response:
            self.user_id = response['user_id']
