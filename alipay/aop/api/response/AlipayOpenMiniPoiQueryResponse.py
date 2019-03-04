#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NearbyAddressInfo import NearbyAddressInfo


class AlipayOpenMiniPoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPoiQueryResponse, self).__init__()
        self._max_count = None
        self._nearby_address_info_list = None
        self._total_count = None

    @property
    def max_count(self):
        return self._max_count

    @max_count.setter
    def max_count(self, value):
        self._max_count = value
    @property
    def nearby_address_info_list(self):
        return self._nearby_address_info_list

    @nearby_address_info_list.setter
    def nearby_address_info_list(self, value):
        if isinstance(value, list):
            self._nearby_address_info_list = list()
            for i in value:
                if isinstance(i, NearbyAddressInfo):
                    self._nearby_address_info_list.append(i)
                else:
                    self._nearby_address_info_list.append(NearbyAddressInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPoiQueryResponse, self).parse_response_content(response_content)
        if 'max_count' in response:
            self.max_count = response['max_count']
        if 'nearby_address_info_list' in response:
            self.nearby_address_info_list = response['nearby_address_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
