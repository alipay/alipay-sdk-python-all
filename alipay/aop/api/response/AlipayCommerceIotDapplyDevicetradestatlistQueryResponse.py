#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceTradeInfoList import DeviceTradeInfoList


class AlipayCommerceIotDapplyDevicetradestatlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyDevicetradestatlistQueryResponse, self).__init__()
        self._devicetradestatlist = None
        self._total_count = None

    @property
    def devicetradestatlist(self):
        return self._devicetradestatlist

    @devicetradestatlist.setter
    def devicetradestatlist(self, value):
        if isinstance(value, DeviceTradeInfoList):
            self._devicetradestatlist = value
        else:
            self._devicetradestatlist = DeviceTradeInfoList.from_alipay_dict(value)
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyDevicetradestatlistQueryResponse, self).parse_response_content(response_content)
        if 'devicetradestatlist' in response:
            self.devicetradestatlist = response['devicetradestatlist']
        if 'total_count' in response:
            self.total_count = response['total_count']
