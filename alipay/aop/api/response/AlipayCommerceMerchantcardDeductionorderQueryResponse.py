#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeductionOrderInfo import DeductionOrderInfo


class AlipayCommerceMerchantcardDeductionorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardDeductionorderQueryResponse, self).__init__()
        self._deduction_order_info = None

    @property
    def deduction_order_info(self):
        return self._deduction_order_info

    @deduction_order_info.setter
    def deduction_order_info(self, value):
        if isinstance(value, DeductionOrderInfo):
            self._deduction_order_info = value
        else:
            self._deduction_order_info = DeductionOrderInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardDeductionorderQueryResponse, self).parse_response_content(response_content)
        if 'deduction_order_info' in response:
            self.deduction_order_info = response['deduction_order_info']
