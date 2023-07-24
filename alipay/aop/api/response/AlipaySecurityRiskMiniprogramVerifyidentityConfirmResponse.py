#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CheckBizData import CheckBizData


class AlipaySecurityRiskMiniprogramVerifyidentityConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskMiniprogramVerifyidentityConfirmResponse, self).__init__()
        self._biz_data = None
        self._verify_result = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, CheckBizData):
            self._biz_data = value
        else:
            self._biz_data = CheckBizData.from_alipay_dict(value)
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskMiniprogramVerifyidentityConfirmResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
        if 'verify_result' in response:
            self.verify_result = response['verify_result']
