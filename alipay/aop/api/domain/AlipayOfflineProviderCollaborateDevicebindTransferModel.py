#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceRecordInfo import DeviceRecordInfo
from alipay.aop.api.domain.DeviceExtAttribute import DeviceExtAttribute


class AlipayOfflineProviderCollaborateDevicebindTransferModel(object):

    def __init__(self):
        self._device_record_files = None
        self._device_sn = None
        self._ext_params = None
        self._old_device_sn = None

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
    @property
    def old_device_sn(self):
        return self._old_device_sn

    @old_device_sn.setter
    def old_device_sn(self, value):
        self._old_device_sn = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.old_device_sn:
            if hasattr(self.old_device_sn, 'to_alipay_dict'):
                params['old_device_sn'] = self.old_device_sn.to_alipay_dict()
            else:
                params['old_device_sn'] = self.old_device_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateDevicebindTransferModel()
        if 'device_record_files' in d:
            o.device_record_files = d['device_record_files']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'old_device_sn' in d:
            o.old_device_sn = d['old_device_sn']
        return o


