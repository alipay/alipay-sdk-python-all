#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerPaymentsPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerPaymentsPayResponse, self).__init__()
        self._order_str = None
        self._pay_order_id = None
        self._result = None

    @property
    def order_str(self):
        return self._order_str

    @order_str.setter
    def order_str(self, value):
        self._order_str = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerPaymentsPayResponse, self).parse_response_content(response_content)
        if 'order_str' in response:
            self.order_str = response['order_str']
        if 'pay_order_id' in response:
            self.pay_order_id = response['pay_order_id']
        if 'result' in response:
            self.result = response['result']
