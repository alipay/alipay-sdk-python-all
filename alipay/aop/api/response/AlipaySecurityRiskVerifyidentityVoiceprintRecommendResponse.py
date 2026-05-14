#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskVerifyidentityVoiceprintRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskVerifyidentityVoiceprintRecommendResponse, self).__init__()
        self._err_code = None
        self._err_msg = None
        self._is_success = None
        self._open_url = None
        self._recommendable = None

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
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def open_url(self):
        return self._open_url

    @open_url.setter
    def open_url(self, value):
        self._open_url = value
    @property
    def recommendable(self):
        return self._recommendable

    @recommendable.setter
    def recommendable(self, value):
        self._recommendable = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskVerifyidentityVoiceprintRecommendResponse, self).parse_response_content(response_content)
        if 'err_code' in response:
            self.err_code = response['err_code']
        if 'err_msg' in response:
            self.err_msg = response['err_msg']
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'open_url' in response:
            self.open_url = response['open_url']
        if 'recommendable' in response:
            self.recommendable = response['recommendable']
