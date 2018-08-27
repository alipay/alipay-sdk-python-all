#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicMessageMatcherSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicMessageMatcherSendResponse, self).__init__()
        self._code = None
        self._msg = None
        self._to_alipay_user_id = None
        self._to_user_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def to_alipay_user_id(self):
        return self._to_alipay_user_id

    @to_alipay_user_id.setter
    def to_alipay_user_id(self, value):
        self._to_alipay_user_id = value
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicMessageMatcherSendResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'to_alipay_user_id' in response:
            self.to_alipay_user_id = response['to_alipay_user_id']
        if 'to_user_id' in response:
            self.to_user_id = response['to_user_id']
