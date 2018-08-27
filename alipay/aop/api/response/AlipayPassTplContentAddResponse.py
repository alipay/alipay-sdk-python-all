#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPassTplContentAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPassTplContentAddResponse, self).__init__()
        self._biz_result = None
        self._error_code = None
        self._success = None

    @property
    def biz_result(self):
        return self._biz_result

    @biz_result.setter
    def biz_result(self, value):
        self._biz_result = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayPassTplContentAddResponse, self).parse_response_content(response_content)
        if 'biz_result' in response:
            self.biz_result = response['biz_result']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'success' in response:
            self.success = response['success']
