#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VehicleInfoDto import VehicleInfoDto


class AlipayEcoMycarVehicleInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarVehicleInfoQueryResponse, self).__init__()
        self._vehicle_list = None

    @property
    def vehicle_list(self):
        return self._vehicle_list

    @vehicle_list.setter
    def vehicle_list(self, value):
        if isinstance(value, list):
            self._vehicle_list = list()
            for i in value:
                if isinstance(i, VehicleInfoDto):
                    self._vehicle_list.append(i)
                else:
                    self._vehicle_list.append(VehicleInfoDto.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarVehicleInfoQueryResponse, self).parse_response_content(response_content)
        if 'vehicle_list' in response:
            self.vehicle_list = response['vehicle_list']
