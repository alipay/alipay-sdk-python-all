#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiFamilyInfoVO import OpenApiFamilyInfoVO
from alipay.aop.api.domain.OpenApiSkuInfoVO import OpenApiSkuInfoVO


class AlipayUserAntstarshipHomeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntstarshipHomeQueryResponse, self).__init__()
        self._end_time = None
        self._family_info = None
        self._sku_info_list = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def family_info(self):
        return self._family_info

    @family_info.setter
    def family_info(self, value):
        if isinstance(value, OpenApiFamilyInfoVO):
            self._family_info = value
        else:
            self._family_info = OpenApiFamilyInfoVO.from_alipay_dict(value)
    @property
    def sku_info_list(self):
        return self._sku_info_list

    @sku_info_list.setter
    def sku_info_list(self, value):
        if isinstance(value, list):
            self._sku_info_list = list()
            for i in value:
                if isinstance(i, OpenApiSkuInfoVO):
                    self._sku_info_list.append(i)
                else:
                    self._sku_info_list.append(OpenApiSkuInfoVO.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntstarshipHomeQueryResponse, self).parse_response_content(response_content)
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'family_info' in response:
            self.family_info = response['family_info']
        if 'sku_info_list' in response:
            self.sku_info_list = response['sku_info_list']
        if 'start_time' in response:
            self.start_time = response['start_time']
