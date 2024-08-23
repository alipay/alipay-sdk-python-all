#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TransferCarResultResp import TransferCarResultResp


class AlipayCommerceTransportCarsaleVehicleModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportCarsaleVehicleModifyResponse, self).__init__()
        self._car_result = None

    @property
    def car_result(self):
        return self._car_result

    @car_result.setter
    def car_result(self, value):
        if isinstance(value, list):
            self._car_result = list()
            for i in value:
                if isinstance(i, TransferCarResultResp):
                    self._car_result.append(i)
                else:
                    self._car_result.append(TransferCarResultResp.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportCarsaleVehicleModifyResponse, self).parse_response_content(response_content)
        if 'car_result' in response:
            self.car_result = response['car_result']
