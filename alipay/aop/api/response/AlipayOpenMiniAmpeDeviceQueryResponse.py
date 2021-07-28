#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeDeviceVO import AmpeDeviceVO


class AlipayOpenMiniAmpeDeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeDeviceQueryResponse, self).__init__()
        self._device_list = None
        self._total_count = None

    @property
    def device_list(self):
        return self._device_list

    @device_list.setter
    def device_list(self, value):
        if isinstance(value, list):
            self._device_list = list()
            for i in value:
                if isinstance(i, AmpeDeviceVO):
                    self._device_list.append(i)
                else:
                    self._device_list.append(AmpeDeviceVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeDeviceQueryResponse, self).parse_response_content(response_content)
        if 'device_list' in response:
            self.device_list = response['device_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
