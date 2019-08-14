#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotAdvertiserDeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotAdvertiserDeviceQueryResponse, self).__init__()
        self._device_sn_list = None
        self._total = None

    @property
    def device_sn_list(self):
        return self._device_sn_list

    @device_sn_list.setter
    def device_sn_list(self, value):
        if isinstance(value, list):
            self._device_sn_list = list()
            for i in value:
                self._device_sn_list.append(i)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotAdvertiserDeviceQueryResponse, self).parse_response_content(response_content)
        if 'device_sn_list' in response:
            self.device_sn_list = response['device_sn_list']
        if 'total' in response:
            self.total = response['total']
