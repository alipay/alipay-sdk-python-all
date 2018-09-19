#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDevice import IotDevice


class AlipayCommerceIotDeviceModifyModel(object):

    def __init__(self):
        self._device = None
        self._protocol_supplier_id = None
        self._user_id = None

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, value):
        if isinstance(value, IotDevice):
            self._device = value
        else:
            self._device = IotDevice.from_alipay_dict(value)
    @property
    def protocol_supplier_id(self):
        return self._protocol_supplier_id

    @protocol_supplier_id.setter
    def protocol_supplier_id(self, value):
        self._protocol_supplier_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device:
            if hasattr(self.device, 'to_alipay_dict'):
                params['device'] = self.device.to_alipay_dict()
            else:
                params['device'] = self.device
        if self.protocol_supplier_id:
            if hasattr(self.protocol_supplier_id, 'to_alipay_dict'):
                params['protocol_supplier_id'] = self.protocol_supplier_id.to_alipay_dict()
            else:
                params['protocol_supplier_id'] = self.protocol_supplier_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceModifyModel()
        if 'device' in d:
            o.device = d['device']
        if 'protocol_supplier_id' in d:
            o.protocol_supplier_id = d['protocol_supplier_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


