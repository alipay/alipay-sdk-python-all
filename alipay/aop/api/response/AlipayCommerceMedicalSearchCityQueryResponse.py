#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProvinceVo import ProvinceVo


class AlipayCommerceMedicalSearchCityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalSearchCityQueryResponse, self).__init__()
        self._province_list = None

    @property
    def province_list(self):
        return self._province_list

    @province_list.setter
    def province_list(self, value):
        if isinstance(value, ProvinceVo):
            self._province_list = value
        else:
            self._province_list = ProvinceVo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalSearchCityQueryResponse, self).parse_response_content(response_content)
        if 'province_list' in response:
            self.province_list = response['province_list']
