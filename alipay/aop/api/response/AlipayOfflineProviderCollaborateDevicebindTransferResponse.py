#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceRecordInfo import DeviceRecordInfo
from alipay.aop.api.domain.DeviceExtAttribute import DeviceExtAttribute


class AlipayOfflineProviderCollaborateDevicebindTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateDevicebindTransferResponse, self).__init__()
        self._device_record_files = None
        self._device_sn = None
        self._ext_params = None
        self._old_device_sn = None

    @property
    def device_record_files(self):
        return self._device_record_files

    @device_record_files.setter
    def device_record_files(self, value):
        if isinstance(value, DeviceRecordInfo):
            self._device_record_files = value
        else:
            self._device_record_files = DeviceRecordInfo.from_alipay_dict(value)
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, DeviceExtAttribute):
            self._ext_params = value
        else:
            self._ext_params = DeviceExtAttribute.from_alipay_dict(value)
    @property
    def old_device_sn(self):
        return self._old_device_sn

    @old_device_sn.setter
    def old_device_sn(self, value):
        self._old_device_sn = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateDevicebindTransferResponse, self).parse_response_content(response_content)
        if 'device_record_files' in response:
            self.device_record_files = response['device_record_files']
        if 'device_sn' in response:
            self.device_sn = response['device_sn']
        if 'ext_params' in response:
            self.ext_params = response['ext_params']
        if 'old_device_sn' in response:
            self.old_device_sn = response['old_device_sn']
