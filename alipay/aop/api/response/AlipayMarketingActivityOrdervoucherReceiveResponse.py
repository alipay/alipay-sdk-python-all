#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderVoucherReceiveResult import OrderVoucherReceiveResult


class AlipayMarketingActivityOrdervoucherReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherReceiveResponse, self).__init__()
        self._receive_result_list = None

    @property
    def receive_result_list(self):
        return self._receive_result_list

    @receive_result_list.setter
    def receive_result_list(self, value):
        if isinstance(value, list):
            self._receive_result_list = list()
            for i in value:
                if isinstance(i, OrderVoucherReceiveResult):
                    self._receive_result_list.append(i)
                else:
                    self._receive_result_list.append(OrderVoucherReceiveResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherReceiveResponse, self).parse_response_content(response_content)
        if 'receive_result_list' in response:
            self.receive_result_list = response['receive_result_list']
