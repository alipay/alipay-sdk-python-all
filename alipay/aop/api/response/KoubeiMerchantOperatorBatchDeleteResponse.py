#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMerchantOperatorBatchDeleteResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantOperatorBatchDeleteResponse, self).__init__()
        self._biz_code = None
        self._success = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantOperatorBatchDeleteResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'success' in response:
            self.success = response['success']
