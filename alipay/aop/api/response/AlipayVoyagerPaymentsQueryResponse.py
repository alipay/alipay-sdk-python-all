#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StandardPayOrderDTO import StandardPayOrderDTO
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerPaymentsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerPaymentsQueryResponse, self).__init__()
        self._pay_order = None
        self._result = None

    @property
    def pay_order(self):
        return self._pay_order

    @pay_order.setter
    def pay_order(self, value):
        if isinstance(value, StandardPayOrderDTO):
            self._pay_order = value
        else:
            self._pay_order = StandardPayOrderDTO.from_alipay_dict(value)
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
        response = super(AlipayVoyagerPaymentsQueryResponse, self).parse_response_content(response_content)
        if 'pay_order' in response:
            self.pay_order = response['pay_order']
        if 'result' in response:
            self.result = response['result']
