#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpRiskIndicatorModel import EpRiskIndicatorModel


class ZhimaCreditEpIndicatorQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpIndicatorQueryResponse, self).__init__()
        self._array_data = None
        self._company_key = None

    @property
    def array_data(self):
        return self._array_data

    @array_data.setter
    def array_data(self, value):
        if isinstance(value, list):
            self._array_data = list()
            for i in value:
                if isinstance(i, EpRiskIndicatorModel):
                    self._array_data.append(i)
                else:
                    self._array_data.append(EpRiskIndicatorModel.from_alipay_dict(i))
    @property
    def company_key(self):
        return self._company_key

    @company_key.setter
    def company_key(self, value):
        self._company_key = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpIndicatorQueryResponse, self).parse_response_content(response_content)
        if 'array_data' in response:
            self.array_data = response['array_data']
        if 'company_key' in response:
            self.company_key = response['company_key']
