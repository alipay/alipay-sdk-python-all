#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperatorData import OperatorData


class AlipayContentCommercialMerchantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentCommercialMerchantQueryResponse, self).__init__()
        self._operator_data = None

    @property
    def operator_data(self):
        return self._operator_data

    @operator_data.setter
    def operator_data(self, value):
        if isinstance(value, list):
            self._operator_data = list()
            for i in value:
                if isinstance(i, OperatorData):
                    self._operator_data.append(i)
                else:
                    self._operator_data.append(OperatorData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayContentCommercialMerchantQueryResponse, self).parse_response_content(response_content)
        if 'operator_data' in response:
            self.operator_data = response['operator_data']
