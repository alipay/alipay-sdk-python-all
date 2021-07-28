#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UpdateCodeResponse import UpdateCodeResponse


class AntMerchantExpandScodeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandScodeModifyResponse, self).__init__()
        self._update_code_response = None

    @property
    def update_code_response(self):
        return self._update_code_response

    @update_code_response.setter
    def update_code_response(self, value):
        if isinstance(value, UpdateCodeResponse):
            self._update_code_response = value
        else:
            self._update_code_response = UpdateCodeResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandScodeModifyResponse, self).parse_response_content(response_content)
        if 'update_code_response' in response:
            self.update_code_response = response['update_code_response']
