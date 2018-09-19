#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AreaInfo import AreaInfo


class AlipayEbppConfigProvinceSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppConfigProvinceSearchResponse, self).__init__()
        self._area_info_result = None

    @property
    def area_info_result(self):
        return self._area_info_result

    @area_info_result.setter
    def area_info_result(self, value):
        if isinstance(value, list):
            self._area_info_result = list()
            for i in value:
                if isinstance(i, AreaInfo):
                    self._area_info_result.append(i)
                else:
                    self._area_info_result.append(AreaInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppConfigProvinceSearchResponse, self).parse_response_content(response_content)
        if 'area_info_result' in response:
            self.area_info_result = response['area_info_result']
