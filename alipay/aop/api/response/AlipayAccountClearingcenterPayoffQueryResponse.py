#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayOffOrderVO import PayOffOrderVO


class AlipayAccountClearingcenterPayoffQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountClearingcenterPayoffQueryResponse, self).__init__()
        self._pay_off_order_list = None
        self._result_code = None
        self._result_description = None
        self._success = None

    @property
    def pay_off_order_list(self):
        return self._pay_off_order_list

    @pay_off_order_list.setter
    def pay_off_order_list(self, value):
        if isinstance(value, list):
            self._pay_off_order_list = list()
            for i in value:
                if isinstance(i, PayOffOrderVO):
                    self._pay_off_order_list.append(i)
                else:
                    self._pay_off_order_list.append(PayOffOrderVO.from_alipay_dict(i))
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_description(self):
        return self._result_description

    @result_description.setter
    def result_description(self, value):
        self._result_description = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountClearingcenterPayoffQueryResponse, self).parse_response_content(response_content)
        if 'pay_off_order_list' in response:
            self.pay_off_order_list = response['pay_off_order_list']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_description' in response:
            self.result_description = response['result_description']
        if 'success' in response:
            self.success = response['success']
