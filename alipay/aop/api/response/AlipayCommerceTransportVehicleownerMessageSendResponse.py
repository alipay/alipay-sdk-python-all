#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VehicleMsgSendResultEntity import VehicleMsgSendResultEntity


class AlipayCommerceTransportVehicleownerMessageSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerMessageSendResponse, self).__init__()
        self._send_result_list = None

    @property
    def send_result_list(self):
        return self._send_result_list

    @send_result_list.setter
    def send_result_list(self, value):
        if isinstance(value, list):
            self._send_result_list = list()
            for i in value:
                if isinstance(i, VehicleMsgSendResultEntity):
                    self._send_result_list.append(i)
                else:
                    self._send_result_list.append(VehicleMsgSendResultEntity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehicleownerMessageSendResponse, self).parse_response_content(response_content)
        if 'send_result_list' in response:
            self.send_result_list = response['send_result_list']
