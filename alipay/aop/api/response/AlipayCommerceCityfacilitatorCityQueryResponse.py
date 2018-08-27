#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CityFunction import CityFunction


class AlipayCommerceCityfacilitatorCityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorCityQueryResponse, self).__init__()
        self._citys = None

    @property
    def citys(self):
        return self._citys

    @citys.setter
    def citys(self, value):
        if isinstance(value, list):
            self._citys = list()
            for i in value:
                if isinstance(i, CityFunction):
                    self._citys.append(i)
                else:
                    self._citys.append(CityFunction.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorCityQueryResponse, self).parse_response_content(response_content)
        if 'citys' in response:
            self.citys = response['citys']
