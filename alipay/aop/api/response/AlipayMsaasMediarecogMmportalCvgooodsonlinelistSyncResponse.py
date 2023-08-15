#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogMmportalCvgooodsonlinelistSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmportalCvgooodsonlinelistSyncResponse, self).__init__()
        self._result = None
        self._ret_code = None
        self._ret_msg = None
        self._ret_success = None

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
    def ret_success(self):
        return self._ret_success

    @ret_success.setter
    def ret_success(self, value):
        self._ret_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmportalCvgooodsonlinelistSyncResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'ret_code' in response:
            self.ret_code = response['ret_code']
        if 'ret_msg' in response:
            self.ret_msg = response['ret_msg']
        if 'ret_success' in response:
            self.ret_success = response['ret_success']
