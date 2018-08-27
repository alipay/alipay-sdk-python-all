#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDevice import IotDevice
from alipay.aop.api.domain.IotDevicePersonalInfo import IotDevicePersonalInfo


class AlipayCommerceIotDevicelistCreateModel(object):

    def __init__(self):
        self._device_list = None
        self._device_personal_info_list = None
        self._protocol_supplier_id = None
        self._user_id = None

    @property
    def device_list(self):
        return self._device_list

    @device_list.setter
    def device_list(self, value):
        if isinstance(value, list):
            self._device_list = list()
            for i in value:
                if isinstance(i, IotDevice):
                    self._device_list.append(i)
                else:
                    self._device_list.append(IotDevice.from_alipay_dict(i))
    @property
    def device_personal_info_list(self):
        return self._device_personal_info_list

    @device_personal_info_list.setter
    def device_personal_info_list(self, value):
        if isinstance(value, list):
            self._device_personal_info_list = list()
            for i in value:
                if isinstance(i, IotDevicePersonalInfo):
                    self._device_personal_info_list.append(i)
                else:
                    self._device_personal_info_list.append(IotDevicePersonalInfo.from_alipay_dict(i))
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
        if self.device_list:
            if isinstance(self.device_list, list):
                for i in range(0, len(self.device_list)):
                    element = self.device_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_list[i] = element.to_alipay_dict()
            if hasattr(self.device_list, 'to_alipay_dict'):
                params['device_list'] = self.device_list.to_alipay_dict()
            else:
                params['device_list'] = self.device_list
        if self.device_personal_info_list:
            if isinstance(self.device_personal_info_list, list):
                for i in range(0, len(self.device_personal_info_list)):
                    element = self.device_personal_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_personal_info_list[i] = element.to_alipay_dict()
            if hasattr(self.device_personal_info_list, 'to_alipay_dict'):
                params['device_personal_info_list'] = self.device_personal_info_list.to_alipay_dict()
            else:
                params['device_personal_info_list'] = self.device_personal_info_list
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
        o = AlipayCommerceIotDevicelistCreateModel()
        if 'device_list' in d:
            o.device_list = d['device_list']
        if 'device_personal_info_list' in d:
            o.device_personal_info_list = d['device_personal_info_list']
        if 'protocol_supplier_id' in d:
            o.protocol_supplier_id = d['protocol_supplier_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


