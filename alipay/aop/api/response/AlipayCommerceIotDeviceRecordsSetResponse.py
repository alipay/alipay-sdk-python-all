#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceRecords import DeviceRecords


class AlipayCommerceIotDeviceRecordsSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceRecordsSetResponse, self).__init__()
        self._device_records = None
        self._device_remark = None

    @property
    def device_records(self):
        return self._device_records

    @device_records.setter
    def device_records(self, value):
        if isinstance(value, DeviceRecords):
            self._device_records = value
        else:
            self._device_records = DeviceRecords.from_alipay_dict(value)
    @property
    def device_remark(self):
        return self._device_remark

    @device_remark.setter
    def device_remark(self, value):
        self._device_remark = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceRecordsSetResponse, self).parse_response_content(response_content)
        if 'device_records' in response:
            self.device_records = response['device_records']
        if 'device_remark' in response:
            self.device_remark = response['device_remark']
