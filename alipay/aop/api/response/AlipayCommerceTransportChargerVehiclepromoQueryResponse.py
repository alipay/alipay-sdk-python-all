#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VehiclePromoResult import VehiclePromoResult


class AlipayCommerceTransportChargerVehiclepromoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerVehiclepromoQueryResponse, self).__init__()
        self._orderStr = None
        self._promos = None

    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value
    @property
    def promos(self):
        return self._promos

    @promos.setter
    def promos(self, value):
        if isinstance(value, list):
            self._promos = list()
            for i in value:
                if isinstance(i, VehiclePromoResult):
                    self._promos.append(i)
                else:
                    self._promos.append(VehiclePromoResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerVehiclepromoQueryResponse, self).parse_response_content(response_content)
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
        if 'promos' in response:
            self.promos = response['promos']
