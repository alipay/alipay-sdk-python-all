#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApplyCodeResponse import ApplyCodeResponse


class AntMerchantExpandScodeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandScodeApplyResponse, self).__init__()
        self._apply_code_response = None

    @property
    def apply_code_response(self):
        return self._apply_code_response

    @apply_code_response.setter
    def apply_code_response(self, value):
        if isinstance(value, ApplyCodeResponse):
            self._apply_code_response = value
        else:
            self._apply_code_response = ApplyCodeResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandScodeApplyResponse, self).parse_response_content(response_content)
        if 'apply_code_response' in response:
            self.apply_code_response = response['apply_code_response']
