#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VehModelDto import VehModelDto


class AlipayEcoMycarVehicleModelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarVehicleModelQueryResponse, self).__init__()
        self._veh_model_list = None

    @property
    def veh_model_list(self):
        return self._veh_model_list

    @veh_model_list.setter
    def veh_model_list(self, value):
        if isinstance(value, list):
            self._veh_model_list = list()
            for i in value:
                if isinstance(i, VehModelDto):
                    self._veh_model_list.append(i)
                else:
                    self._veh_model_list.append(VehModelDto.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarVehicleModelQueryResponse, self).parse_response_content(response_content)
        if 'veh_model_list' in response:
            self.veh_model_list = response['veh_model_list']
