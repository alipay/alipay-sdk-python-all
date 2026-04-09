#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CrossBorderEcomCompanyDetail import CrossBorderEcomCompanyDetail


class ZhimaCreditEpCbecomdetailPersonQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCbecomdetailPersonQueryResponse, self).__init__()
        self._array_data = None

    @property
    def array_data(self):
        return self._array_data

    @array_data.setter
    def array_data(self, value):
        if isinstance(value, list):
            self._array_data = list()
            for i in value:
                if isinstance(i, CrossBorderEcomCompanyDetail):
                    self._array_data.append(i)
                else:
                    self._array_data.append(CrossBorderEcomCompanyDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCbecomdetailPersonQueryResponse, self).parse_response_content(response_content)
        if 'array_data' in response:
            self.array_data = response['array_data']
