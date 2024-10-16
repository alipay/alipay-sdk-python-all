#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardDeductionorderUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardDeductionorderUseResponse, self).__init__()
        self._deduction_order_id = None

    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardDeductionorderUseResponse, self).parse_response_content(response_content)
        if 'deduction_order_id' in response:
            self.deduction_order_id = response['deduction_order_id']
