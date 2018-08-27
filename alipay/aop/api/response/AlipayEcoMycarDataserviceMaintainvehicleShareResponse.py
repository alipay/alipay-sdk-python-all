#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MaintainVehicleInfo import MaintainVehicleInfo


class AlipayEcoMycarDataserviceMaintainvehicleShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarDataserviceMaintainvehicleShareResponse, self).__init__()
        self._info = None

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        if isinstance(value, MaintainVehicleInfo):
            self._info = value
        else:
            self._info = MaintainVehicleInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarDataserviceMaintainvehicleShareResponse, self).parse_response_content(response_content)
        if 'info' in response:
            self.info = response['info']
