#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcenterpriseVehicleModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseVehicleModifyResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._vehicle_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseVehicleModifyResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'vehicle_id' in response:
            self.vehicle_id = response['vehicle_id']
