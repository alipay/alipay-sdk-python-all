#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResponseModelForPaymentInstruction import ResponseModelForPaymentInstruction


class AlipayBossFncGfsmartpayPaymentinstructionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfsmartpayPaymentinstructionQueryResponse, self).__init__()
        self._result_set = None

    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, ResponseModelForPaymentInstruction):
            self._result_set = value
        else:
            self._result_set = ResponseModelForPaymentInstruction.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfsmartpayPaymentinstructionQueryResponse, self).parse_response_content(response_content)
        if 'result_set' in response:
            self.result_set = response['result_set']
