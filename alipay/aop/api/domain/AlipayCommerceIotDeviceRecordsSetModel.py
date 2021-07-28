#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceRecordFile import DeviceRecordFile
from alipay.aop.api.domain.DeviceExtParams import DeviceExtParams


class AlipayCommerceIotDeviceRecordsSetModel(object):

    def __init__(self):
        self._device_record_files = None
        self._ext_params = None
        self._scene_code = None
        self._scene_params = None
        self._sn = None
        self._supplier_id = None

    @property
    def device_record_files(self):
        return self._device_record_files

    @device_record_files.setter
    def device_record_files(self, value):
        if isinstance(value, list):
            self._device_record_files = list()
            for i in value:
                if isinstance(i, DeviceRecordFile):
                    self._device_record_files.append(i)
                else:
                    self._device_record_files.append(DeviceRecordFile.from_alipay_dict(i))
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, DeviceExtParams):
            self._ext_params = value
        else:
            self._ext_params = DeviceExtParams.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_params(self):
        return self._scene_params

    @scene_params.setter
    def scene_params(self, value):
        self._scene_params = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


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
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_params:
            if hasattr(self.scene_params, 'to_alipay_dict'):
                params['scene_params'] = self.scene_params.to_alipay_dict()
            else:
                params['scene_params'] = self.scene_params
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceRecordsSetModel()
        if 'device_record_files' in d:
            o.device_record_files = d['device_record_files']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_params' in d:
            o.scene_params = d['scene_params']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


