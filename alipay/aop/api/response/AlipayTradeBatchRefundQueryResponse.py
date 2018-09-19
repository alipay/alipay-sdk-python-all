#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BatchRefundDetailResult import BatchRefundDetailResult


class AlipayTradeBatchRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeBatchRefundQueryResponse, self).__init__()
        self._result_details = None

    @property
    def result_details(self):
        return self._result_details

    @result_details.setter
    def result_details(self, value):
        if isinstance(value, list):
            self._result_details = list()
            for i in value:
                if isinstance(i, BatchRefundDetailResult):
                    self._result_details.append(i)
                else:
                    self._result_details.append(BatchRefundDetailResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeBatchRefundQueryResponse, self).parse_response_content(response_content)
        if 'result_details' in response:
            self.result_details = response['result_details']
