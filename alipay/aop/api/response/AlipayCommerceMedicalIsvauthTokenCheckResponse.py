#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IsvAuthResult import IsvAuthResult


class AlipayCommerceMedicalIsvauthTokenCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIsvauthTokenCheckResponse, self).__init__()
        self._isv_auth_result = None

    @property
    def isv_auth_result(self):
        return self._isv_auth_result

    @isv_auth_result.setter
    def isv_auth_result(self, value):
        if isinstance(value, IsvAuthResult):
            self._isv_auth_result = value
        else:
            self._isv_auth_result = IsvAuthResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIsvauthTokenCheckResponse, self).parse_response_content(response_content)
        if 'isv_auth_result' in response:
            self.isv_auth_result = response['isv_auth_result']
