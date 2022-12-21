#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogMmportalCvgoodsSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmportalCvgoodsSyncResponse, self).__init__()
        self._result = None
        self._ret_code = None
        self._ret_msg = None
        self._success = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def ret_code(self):
        return self._ret_code

    @ret_code.setter
    def ret_code(self, value):
        self._ret_code = value
    @property
    def ret_msg(self):
        return self._ret_msg

    @ret_msg.setter
    def ret_msg(self, value):
        self._ret_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmportalCvgoodsSyncResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'ret_code' in response:
            self.ret_code = response['ret_code']
        if 'ret_msg' in response:
            self.ret_msg = response['ret_msg']
        if 'success' in response:
            self.success = response['success']
