#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeductionOrderInfo import DeductionOrderInfo
from alipay.aop.api.domain.DeductionRefundOrderInfo import DeductionRefundOrderInfo


class AlipayCommerceMerchantcardDeductionorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardDeductionorderQueryResponse, self).__init__()
        self._deduction_order_info = None
        self._deduction_refund_order_info_list = None

    @property
    def deduction_order_info(self):
        return self._deduction_order_info

    @deduction_order_info.setter
    def deduction_order_info(self, value):
        if isinstance(value, DeductionOrderInfo):
            self._deduction_order_info = value
        else:
            self._deduction_order_info = DeductionOrderInfo.from_alipay_dict(value)
    @property
    def deduction_refund_order_info_list(self):
        return self._deduction_refund_order_info_list

    @deduction_refund_order_info_list.setter
    def deduction_refund_order_info_list(self, value):
        if isinstance(value, list):
            self._deduction_refund_order_info_list = list()
            for i in value:
                if isinstance(i, DeductionRefundOrderInfo):
                    self._deduction_refund_order_info_list.append(i)
                else:
                    self._deduction_refund_order_info_list.append(DeductionRefundOrderInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardDeductionorderQueryResponse, self).parse_response_content(response_content)
        if 'deduction_order_info' in response:
            self.deduction_order_info = response['deduction_order_info']
        if 'deduction_refund_order_info_list' in response:
            self.deduction_refund_order_info_list = response['deduction_refund_order_info_list']
