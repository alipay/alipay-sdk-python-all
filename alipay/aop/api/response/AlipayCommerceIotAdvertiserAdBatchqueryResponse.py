#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreationPlanData import CreationPlanData


class AlipayCommerceIotAdvertiserAdBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotAdvertiserAdBatchqueryResponse, self).__init__()
        self._result = None
        self._total = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, CreationPlanData):
                    self._result.append(i)
                else:
                    self._result.append(CreationPlanData.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotAdvertiserAdBatchqueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'total' in response:
            self.total = response['total']
