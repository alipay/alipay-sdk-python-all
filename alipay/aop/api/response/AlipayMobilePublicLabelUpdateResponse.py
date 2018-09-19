#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicLabelUpdateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicLabelUpdateResponse, self).__init__()
        self._code = None
        self._id = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicLabelUpdateResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'id' in response:
            self.id = response['id']
        if 'msg' in response:
            self.msg = response['msg']
