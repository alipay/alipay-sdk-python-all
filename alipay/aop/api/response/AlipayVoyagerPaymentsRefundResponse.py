#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerPaymentsRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerPaymentsRefundResponse, self).__init__()
        self._refund_amount = None
        self._refund_order_id = None
        self._refund_time = None
        self._result = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._refund_amount = value
        else:
            self._refund_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
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
        response = super(AlipayVoyagerPaymentsRefundResponse, self).parse_response_content(response_content)
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_order_id' in response:
            self.refund_order_id = response['refund_order_id']
        if 'refund_time' in response:
            self.refund_time = response['refund_time']
        if 'result' in response:
            self.result = response['result']
