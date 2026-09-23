#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpPromoInfo import OpPromoInfo


class AlipayPayAppOperationPromoTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppOperationPromoTriggerResponse, self).__init__()
        self._operation_promo_list = None
        self._pay_operation_info = None

    @property
    def operation_promo_list(self):
        return self._operation_promo_list

    @operation_promo_list.setter
    def operation_promo_list(self, value):
        if isinstance(value, list):
            self._operation_promo_list = list()
            for i in value:
                if isinstance(i, OpPromoInfo):
                    self._operation_promo_list.append(i)
                else:
                    self._operation_promo_list.append(OpPromoInfo.from_alipay_dict(i))
    @property
    def pay_operation_info(self):
        return self._pay_operation_info

    @pay_operation_info.setter
    def pay_operation_info(self, value):
        self._pay_operation_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppOperationPromoTriggerResponse, self).parse_response_content(response_content)
        if 'operation_promo_list' in response:
            self.operation_promo_list = response['operation_promo_list']
        if 'pay_operation_info' in response:
            self.pay_operation_info = response['pay_operation_info']
