#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UnitTraffic import UnitTraffic


class AntfortuneStockTrafficQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockTrafficQueryResponse, self).__init__()
        self._traffic_mode = None
        self._units = None

    @property
    def traffic_mode(self):
        return self._traffic_mode

    @traffic_mode.setter
    def traffic_mode(self, value):
        self._traffic_mode = value
    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        if isinstance(value, list):
            self._units = list()
            for i in value:
                if isinstance(i, UnitTraffic):
                    self._units.append(i)
                else:
                    self._units.append(UnitTraffic.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockTrafficQueryResponse, self).parse_response_content(response_content)
        if 'traffic_mode' in response:
            self.traffic_mode = response['traffic_mode']
        if 'units' in response:
            self.units = response['units']
