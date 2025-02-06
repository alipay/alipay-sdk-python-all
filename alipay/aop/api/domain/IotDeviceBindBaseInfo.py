#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceRecordInfo import DeviceRecordInfo
from alipay.aop.api.domain.DeviceExtAttribute import DeviceExtAttribute


class IotDeviceBindBaseInfo(object):

    def __init__(self):
        self._device_bind_status = None
        self._device_record_files = None
        self._device_sn = None
        self._ext_params = None

    @property
    def device_bind_status(self):
        return self._device_bind_status

    @device_bind_status.setter
    def device_bind_status(self, value):
        self._device_bind_status = value
    @property
    def device_record_files(self):
        return self._device_record_files

    @device_record_files.setter
    def device_record_files(self, value):
        if isinstance(value, list):
            self._device_record_files = list()
            for i in value:
                if isinstance(i, DeviceRecordInfo):
                    self._device_record_files.append(i)
                else:
                    self._device_record_files.append(DeviceRecordInfo.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.device_bind_status:
            if hasattr(self.device_bind_status, 'to_alipay_dict'):
                params['device_bind_status'] = self.device_bind_status.to_alipay_dict()
            else:
                params['device_bind_status'] = self.device_bind_status
        if self.device_record_files:
            if isinstance(self.device_record_files, list):
                for i in range(0, len(self.device_record_files)):
                    element = self.device_record_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_record_files[i] = element.to_alipay_dict()
            if hasattr(self.device_record_files, 'to_alipay_dict'):
                params['device_record_files'] = self.device_record_files.to_alipay_dict()
            else:
                params['device_record_files'] = self.device_record_files
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotDeviceBindBaseInfo()
        if 'device_bind_status' in d:
            o.device_bind_status = d['device_bind_status']
        if 'device_record_files' in d:
            o.device_record_files = d['device_record_files']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        return o


