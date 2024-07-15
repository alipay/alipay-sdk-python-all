#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderDiscountDetailInfo import OrderDiscountDetailInfo


class AlipayOpenMiniPromodecisionOrderconsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPromodecisionOrderconsultQueryResponse, self).__init__()
        self._order_discount_detail_info = None
        self._result_code = None

    @property
    def order_discount_detail_info(self):
        return self._order_discount_detail_info

    @order_discount_detail_info.setter
    def order_discount_detail_info(self, value):
        if isinstance(value, OrderDiscountDetailInfo):
            self._order_discount_detail_info = value
        else:
            self._order_discount_detail_info = OrderDiscountDetailInfo.from_alipay_dict(value)
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPromodecisionOrderconsultQueryResponse, self).parse_response_content(response_content)
        if 'order_discount_detail_info' in response:
            self.order_discount_detail_info = response['order_discount_detail_info']
        if 'result_code' in response:
            self.result_code = response['result_code']
