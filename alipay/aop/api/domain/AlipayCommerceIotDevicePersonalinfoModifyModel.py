#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDevicePersonalInfo import IotDevicePersonalInfo


class AlipayCommerceIotDevicePersonalinfoModifyModel(object):

    def __init__(self):
        self._device_personal_info = None
        self._protocol_supplier_id = None
        self._user_id = None

    @property
    def device_personal_info(self):
        return self._device_personal_info

    @device_personal_info.setter
    def device_personal_info(self, value):
        if isinstance(value, IotDevicePersonalInfo):
            self._device_personal_info = value
        else:
            self._device_personal_info = IotDevicePersonalInfo.from_alipay_dict(value)
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
        if self.device_personal_info:
            if hasattr(self.device_personal_info, 'to_alipay_dict'):
                params['device_personal_info'] = self.device_personal_info.to_alipay_dict()
            else:
                params['device_personal_info'] = self.device_personal_info
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
        o = AlipayCommerceIotDevicePersonalinfoModifyModel()
        if 'device_personal_info' in d:
            o.device_personal_info = d['device_personal_info']
        if 'protocol_supplier_id' in d:
            o.protocol_supplier_id = d['protocol_supplier_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


