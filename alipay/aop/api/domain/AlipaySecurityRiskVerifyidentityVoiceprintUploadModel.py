#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskVerifyidentityVoiceprintUploadModel(object):

    def __init__(self):
        self._data_type_name = None
        self._device_id = None
        self._device_info = None
        self._device_version = None
        self._time_stamp = None

    @property
    def data_type_name(self):
        return self._data_type_name

    @data_type_name.setter
    def data_type_name(self, value):
        self._data_type_name = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        self._device_info = value
    @property
    def device_version(self):
        return self._device_version

    @device_version.setter
    def device_version(self, value):
        self._device_version = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_type_name:
            if hasattr(self.data_type_name, 'to_alipay_dict'):
                params['data_type_name'] = self.data_type_name.to_alipay_dict()
            else:
                params['data_type_name'] = self.data_type_name
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.device_version:
            if hasattr(self.device_version, 'to_alipay_dict'):
                params['device_version'] = self.device_version.to_alipay_dict()
            else:
                params['device_version'] = self.device_version
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskVerifyidentityVoiceprintUploadModel()
        if 'data_type_name' in d:
            o.data_type_name = d['data_type_name']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'device_version' in d:
            o.device_version = d['device_version']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


