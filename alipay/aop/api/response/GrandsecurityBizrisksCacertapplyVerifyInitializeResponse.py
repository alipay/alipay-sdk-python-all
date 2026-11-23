#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class GrandsecurityBizrisksCacertapplyVerifyInitializeResponse(AlipayResponse):

    def __init__(self):
        super(GrandsecurityBizrisksCacertapplyVerifyInitializeResponse, self).__init__()
        self._error_code = None
        self._error_msg = None
        self._ext_params = None
        self._init_success = None
        self._verify_id = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def init_success(self):
        return self._init_success

    @init_success.setter
    def init_success(self, value):
        self._init_success = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value

    def parse_response_content(self, response_content):
        response = super(GrandsecurityBizrisksCacertapplyVerifyInitializeResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'ext_params' in response:
            self.ext_params = response['ext_params']
        if 'init_success' in response:
            self.init_success = response['init_success']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
