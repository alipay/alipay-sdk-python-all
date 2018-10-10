#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PlateInfoForYiCai import PlateInfoForYiCai


class AntfortuneQuotationPlateIndexQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneQuotationPlateIndexQueryResponse, self).__init__()
        self._plate_list = None
        self._res = None

    @property
    def plate_list(self):
        return self._plate_list

    @plate_list.setter
    def plate_list(self, value):
        if isinstance(value, list):
            self._plate_list = list()
            for i in value:
                if isinstance(i, PlateInfoForYiCai):
                    self._plate_list.append(i)
                else:
                    self._plate_list.append(PlateInfoForYiCai.from_alipay_dict(i))
    @property
    def res(self):
        return self._res

    @res.setter
    def res(self, value):
        self._res = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneQuotationPlateIndexQueryResponse, self).parse_response_content(response_content)
        if 'plate_list' in response:
            self.plate_list = response['plate_list']
        if 'res' in response:
            self.res = response['res']
