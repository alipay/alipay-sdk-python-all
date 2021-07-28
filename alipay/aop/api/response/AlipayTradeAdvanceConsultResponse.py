#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WaitRepaymentOrderInfo import WaitRepaymentOrderInfo


class AlipayTradeAdvanceConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeAdvanceConsultResponse, self).__init__()
        self._refer_result = None
        self._result_code = None
        self._result_message = None
        self._risk_level = None
        self._wait_repayment_amount = None
        self._wait_repayment_order_count = None
        self._wait_repayment_order_infos = None

    @property
    def refer_result(self):
        return self._refer_result

    @refer_result.setter
    def refer_result(self, value):
        self._refer_result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def wait_repayment_amount(self):
        return self._wait_repayment_amount

    @wait_repayment_amount.setter
    def wait_repayment_amount(self, value):
        self._wait_repayment_amount = value
    @property
    def wait_repayment_order_count(self):
        return self._wait_repayment_order_count

    @wait_repayment_order_count.setter
    def wait_repayment_order_count(self, value):
        self._wait_repayment_order_count = value
    @property
    def wait_repayment_order_infos(self):
        return self._wait_repayment_order_infos

    @wait_repayment_order_infos.setter
    def wait_repayment_order_infos(self, value):
        if isinstance(value, list):
            self._wait_repayment_order_infos = list()
            for i in value:
                if isinstance(i, WaitRepaymentOrderInfo):
                    self._wait_repayment_order_infos.append(i)
                else:
                    self._wait_repayment_order_infos.append(WaitRepaymentOrderInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeAdvanceConsultResponse, self).parse_response_content(response_content)
        if 'refer_result' in response:
            self.refer_result = response['refer_result']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
        if 'risk_level' in response:
            self.risk_level = response['risk_level']
        if 'wait_repayment_amount' in response:
            self.wait_repayment_amount = response['wait_repayment_amount']
        if 'wait_repayment_order_count' in response:
            self.wait_repayment_order_count = response['wait_repayment_order_count']
        if 'wait_repayment_order_infos' in response:
            self.wait_repayment_order_infos = response['wait_repayment_order_infos']
