#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceServiceBaseVO import DeviceServiceBaseVO
from alipay.aop.api.domain.DeviceServiceBaseVO import DeviceServiceBaseVO


class DeviceServiceVO(object):

    def __init__(self):
        self._device_service_base = None
        self._parent_base = None
        self._service_key = None
        self._version_no = None

    @property
    def device_service_base(self):
        return self._device_service_base

    @device_service_base.setter
    def device_service_base(self, value):
        if isinstance(value, DeviceServiceBaseVO):
            self._device_service_base = value
        else:
            self._device_service_base = DeviceServiceBaseVO.from_alipay_dict(value)
    @property
    def parent_base(self):
        return self._parent_base

    @parent_base.setter
    def parent_base(self, value):
        if isinstance(value, DeviceServiceBaseVO):
            self._parent_base = value
        else:
            self._parent_base = DeviceServiceBaseVO.from_alipay_dict(value)
    @property
    def service_key(self):
        return self._service_key

    @service_key.setter
    def service_key(self, value):
        self._service_key = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_service_base:
            if hasattr(self.device_service_base, 'to_alipay_dict'):
                params['device_service_base'] = self.device_service_base.to_alipay_dict()
            else:
                params['device_service_base'] = self.device_service_base
        if self.parent_base:
            if hasattr(self.parent_base, 'to_alipay_dict'):
                params['parent_base'] = self.parent_base.to_alipay_dict()
            else:
                params['parent_base'] = self.parent_base
        if self.service_key:
            if hasattr(self.service_key, 'to_alipay_dict'):
                params['service_key'] = self.service_key.to_alipay_dict()
            else:
                params['service_key'] = self.service_key
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceServiceVO()
        if 'device_service_base' in d:
            o.device_service_base = d['device_service_base']
        if 'parent_base' in d:
            o.parent_base = d['parent_base']
        if 'service_key' in d:
            o.service_key = d['service_key']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


