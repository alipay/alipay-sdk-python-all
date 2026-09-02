#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaleForceAmountConvertResponse import SaleForceAmountConvertResponse


class AnttechOceanbaseObglobalSfamountconvertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalSfamountconvertQueryResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, SaleForceAmountConvertResponse):
            self._result = value
        else:
            self._result = SaleForceAmountConvertResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalSfamountconvertQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
