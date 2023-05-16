#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcAreaInfo import EcAreaInfo
from alipay.aop.api.domain.EcAreaInfo import EcAreaInfo
from alipay.aop.api.domain.EcAreaInfo import EcAreaInfo


class AlipayCommerceEcDistrictQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcDistrictQueryResponse, self).__init__()
        self._city_list = None
        self._district_list = None
        self._province_list = None

    @property
    def city_list(self):
        return self._city_list

    @city_list.setter
    def city_list(self, value):
        if isinstance(value, list):
            self._city_list = list()
            for i in value:
                if isinstance(i, EcAreaInfo):
                    self._city_list.append(i)
                else:
                    self._city_list.append(EcAreaInfo.from_alipay_dict(i))
    @property
    def district_list(self):
        return self._district_list

    @district_list.setter
    def district_list(self, value):
        if isinstance(value, list):
            self._district_list = list()
            for i in value:
                if isinstance(i, EcAreaInfo):
                    self._district_list.append(i)
                else:
                    self._district_list.append(EcAreaInfo.from_alipay_dict(i))
    @property
    def province_list(self):
        return self._province_list

    @province_list.setter
    def province_list(self, value):
        if isinstance(value, list):
            self._province_list = list()
            for i in value:
                if isinstance(i, EcAreaInfo):
                    self._province_list.append(i)
                else:
                    self._province_list.append(EcAreaInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcDistrictQueryResponse, self).parse_response_content(response_content)
        if 'city_list' in response:
            self.city_list = response['city_list']
        if 'district_list' in response:
            self.district_list = response['district_list']
        if 'province_list' in response:
            self.province_list = response['province_list']
