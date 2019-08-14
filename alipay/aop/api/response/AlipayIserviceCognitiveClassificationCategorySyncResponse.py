#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveClassificationCategorySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveClassificationCategorySyncResponse, self).__init__()
        self._err_code = None
        self._err_msg = None
        self._success = None

    @property
    def err_code(self):
        return self._err_code

    @err_code.setter
    def err_code(self, value):
        self._err_code = value
    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveClassificationCategorySyncResponse, self).parse_response_content(response_content)
        if 'err_code' in response:
            self.err_code = response['err_code']
        if 'err_msg' in response:
            self.err_msg = response['err_msg']
        if 'success' in response:
            self.success = response['success']
