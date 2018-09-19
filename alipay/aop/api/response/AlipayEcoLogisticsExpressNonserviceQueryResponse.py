#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AreaCode import AreaCode


class AlipayEcoLogisticsExpressNonserviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoLogisticsExpressNonserviceQueryResponse, self).__init__()
        self._area_codes = None

    @property
    def area_codes(self):
        return self._area_codes

    @area_codes.setter
    def area_codes(self, value):
        if isinstance(value, list):
            self._area_codes = list()
            for i in value:
                if isinstance(i, AreaCode):
                    self._area_codes.append(i)
                else:
                    self._area_codes.append(AreaCode.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoLogisticsExpressNonserviceQueryResponse, self).parse_response_content(response_content)
        if 'area_codes' in response:
            self.area_codes = response['area_codes']
