#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectOnlineModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectOnlineModifyResponse, self).__init__()
        self._sub_merchant_id = None

    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectOnlineModifyResponse, self).parse_response_content(response_content)
        if 'sub_merchant_id' in response:
            self.sub_merchant_id = response['sub_merchant_id']
