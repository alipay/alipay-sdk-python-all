#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InternetbarDeviceActivityData import InternetbarDeviceActivityData


class AlipayEbppIndustryInternetbarDevicedataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryInternetbarDevicedataQueryResponse, self).__init__()
        self._device_activity_data = None
        self._total_count = None

    @property
    def device_activity_data(self):
        return self._device_activity_data

    @device_activity_data.setter
    def device_activity_data(self, value):
        if isinstance(value, list):
            self._device_activity_data = list()
            for i in value:
                if isinstance(i, InternetbarDeviceActivityData):
                    self._device_activity_data.append(i)
                else:
                    self._device_activity_data.append(InternetbarDeviceActivityData.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryInternetbarDevicedataQueryResponse, self).parse_response_content(response_content)
        if 'device_activity_data' in response:
            self.device_activity_data = response['device_activity_data']
        if 'total_count' in response:
            self.total_count = response['total_count']
