#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceApplyOrderDeviceModel import DeviceApplyOrderDeviceModel


class AlipayCommerceIotDapplyOrderdeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyOrderdeviceQueryResponse, self).__init__()
        self._device_infos = None

    @property
    def device_infos(self):
        return self._device_infos

    @device_infos.setter
    def device_infos(self, value):
        if isinstance(value, list):
            self._device_infos = list()
            for i in value:
                if isinstance(i, DeviceApplyOrderDeviceModel):
                    self._device_infos.append(i)
                else:
                    self._device_infos.append(DeviceApplyOrderDeviceModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyOrderdeviceQueryResponse, self).parse_response_content(response_content)
        if 'device_infos' in response:
            self.device_infos = response['device_infos']
