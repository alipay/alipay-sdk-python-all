#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandDigitalgroupApplyModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandDigitalgroupApplyModifyResponse, self).__init__()
        self._apply_order_id = None

    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandDigitalgroupApplyModifyResponse, self).parse_response_content(response_content)
        if 'apply_order_id' in response:
            self.apply_order_id = response['apply_order_id']
