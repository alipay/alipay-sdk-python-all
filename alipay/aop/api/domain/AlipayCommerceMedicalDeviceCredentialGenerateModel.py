#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceIdentityCredentialOpenApiDevice import DeviceIdentityCredentialOpenApiDevice


class AlipayCommerceMedicalDeviceCredentialGenerateModel(object):

    def __init__(self):
        self._devices = None
        self._item_id = None
        self._role_source = None

    @property
    def devices(self):
        return self._devices

    @devices.setter
    def devices(self, value):
        if isinstance(value, list):
            self._devices = list()
            for i in value:
                if isinstance(i, DeviceIdentityCredentialOpenApiDevice):
                    self._devices.append(i)
                else:
                    self._devices.append(DeviceIdentityCredentialOpenApiDevice.from_alipay_dict(i))
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def role_source(self):
        return self._role_source

    @role_source.setter
    def role_source(self, value):
        self._role_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.devices:
            if isinstance(self.devices, list):
                for i in range(0, len(self.devices)):
                    element = self.devices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.devices[i] = element.to_alipay_dict()
            if hasattr(self.devices, 'to_alipay_dict'):
                params['devices'] = self.devices.to_alipay_dict()
            else:
                params['devices'] = self.devices
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.role_source:
            if hasattr(self.role_source, 'to_alipay_dict'):
                params['role_source'] = self.role_source.to_alipay_dict()
            else:
                params['role_source'] = self.role_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDeviceCredentialGenerateModel()
        if 'devices' in d:
            o.devices = d['devices']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'role_source' in d:
            o.role_source = d['role_source']
        return o


