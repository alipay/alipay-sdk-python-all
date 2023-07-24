#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InitBizData import InitBizData


class AlipaySecurityRiskMiniprogramVerifyidentityInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskMiniprogramVerifyidentityInitializeResponse, self).__init__()
        self._biz_data = None
        self._verify_token = None
        self._verify_url = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, InitBizData):
            self._biz_data = value
        else:
            self._biz_data = InitBizData.from_alipay_dict(value)
    @property
    def verify_token(self):
        return self._verify_token

    @verify_token.setter
    def verify_token(self, value):
        self._verify_token = value
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskMiniprogramVerifyidentityInitializeResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
        if 'verify_token' in response:
            self.verify_token = response['verify_token']
        if 'verify_url' in response:
            self.verify_url = response['verify_url']
