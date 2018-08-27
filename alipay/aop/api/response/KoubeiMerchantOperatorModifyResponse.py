#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMerchantOperatorModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantOperatorModifyResponse, self).__init__()
        self._operator_id = None

    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantOperatorModifyResponse, self).parse_response_content(response_content)
        if 'operator_id' in response:
            self.operator_id = response['operator_id']
