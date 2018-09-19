#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicMessageGroupResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicMessageGroupResponse, self).__init__()
        self._code = None
        self._data = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicMessageGroupResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'data' in response:
            self.data = response['data']
        if 'msg' in response:
            self.msg = response['msg']
