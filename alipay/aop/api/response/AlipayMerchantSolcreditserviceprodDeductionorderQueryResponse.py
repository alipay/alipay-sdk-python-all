#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeductionOrderDTO import DeductionOrderDTO


class AlipayMerchantSolcreditserviceprodDeductionorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodDeductionorderQueryResponse, self).__init__()
        self._deduction_order_list = None

    @property
    def deduction_order_list(self):
        return self._deduction_order_list

    @deduction_order_list.setter
    def deduction_order_list(self, value):
        if isinstance(value, list):
            self._deduction_order_list = list()
            for i in value:
                if isinstance(i, DeductionOrderDTO):
                    self._deduction_order_list.append(i)
                else:
                    self._deduction_order_list.append(DeductionOrderDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodDeductionorderQueryResponse, self).parse_response_content(response_content)
        if 'deduction_order_list' in response:
            self.deduction_order_list = response['deduction_order_list']
