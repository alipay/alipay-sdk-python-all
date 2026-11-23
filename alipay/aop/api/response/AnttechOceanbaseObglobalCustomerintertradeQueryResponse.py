#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CustomerIntertradeQueryResponse import CustomerIntertradeQueryResponse


class AnttechOceanbaseObglobalCustomerintertradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalCustomerintertradeQueryResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, CustomerIntertradeQueryResponse):
            self._result = value
        else:
            self._result = CustomerIntertradeQueryResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalCustomerintertradeQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
