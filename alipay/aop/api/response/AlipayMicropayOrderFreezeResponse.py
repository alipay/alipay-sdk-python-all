#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MicroPayOrderDetail import MicroPayOrderDetail


class AlipayMicropayOrderFreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMicropayOrderFreezeResponse, self).__init__()
        self._micro_pay_order_detail = None

    @property
    def micro_pay_order_detail(self):
        return self._micro_pay_order_detail

    @micro_pay_order_detail.setter
    def micro_pay_order_detail(self, value):
        if isinstance(value, MicroPayOrderDetail):
            self._micro_pay_order_detail = value
        else:
            self._micro_pay_order_detail = MicroPayOrderDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMicropayOrderFreezeResponse, self).parse_response_content(response_content)
        if 'micro_pay_order_detail' in response:
            self.micro_pay_order_detail = response['micro_pay_order_detail']
