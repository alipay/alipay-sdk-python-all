#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDdtJhjtestCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDdtJhjtestCreateResponse, self).__init__()
        self._ot_a = None
        self._output_a = None
        self._user_id = None
        self._user_id_openid = None

    @property
    def ot_a(self):
        return self._ot_a

    @ot_a.setter
    def ot_a(self, value):
        self._ot_a = value
    @property
    def output_a(self):
        return self._output_a

    @output_a.setter
    def output_a(self, value):
        self._output_a = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_openid(self):
        return self._user_id_openid

    @user_id_openid.setter
    def user_id_openid(self, value):
        self._user_id_openid = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDdtJhjtestCreateResponse, self).parse_response_content(response_content)
        if 'ot_a' in response:
            self.ot_a = response['ot_a']
        if 'output_a' in response:
            self.output_a = response['output_a']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_id_openid' in response:
            self.user_id_openid = response['user_id_openid']
