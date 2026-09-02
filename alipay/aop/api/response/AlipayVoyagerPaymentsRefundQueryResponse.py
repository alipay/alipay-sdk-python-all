#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StandardRefundOrderDTO import StandardRefundOrderDTO
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerPaymentsRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerPaymentsRefundQueryResponse, self).__init__()
        self._refund_order = None
        self._result = None

    @property
    def refund_order(self):
        return self._refund_order

    @refund_order.setter
    def refund_order(self, value):
        if isinstance(value, StandardRefundOrderDTO):
            self._refund_order = value
        else:
            self._refund_order = StandardRefundOrderDTO.from_alipay_dict(value)
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
        response = super(AlipayVoyagerPaymentsRefundQueryResponse, self).parse_response_content(response_content)
        if 'refund_order' in response:
            self.refund_order = response['refund_order']
        if 'result' in response:
            self.result = response['result']
