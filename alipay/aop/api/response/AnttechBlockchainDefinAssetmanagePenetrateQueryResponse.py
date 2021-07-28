#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinAssetmanagePenetrateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinAssetmanagePenetrateQueryResponse, self).__init__()
        self._error_code = None
        self._error_msg = None
        self._error_view_msg = None
        self._result_obj = None

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
    def error_view_msg(self):
        return self._error_view_msg

    @error_view_msg.setter
    def error_view_msg(self, value):
        self._error_view_msg = value
    @property
    def result_obj(self):
        return self._result_obj

    @result_obj.setter
    def result_obj(self, value):
        self._result_obj = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinAssetmanagePenetrateQueryResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'error_view_msg' in response:
            self.error_view_msg = response['error_view_msg']
        if 'result_obj' in response:
            self.result_obj = response['result_obj']
