#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDevicePrincipal import IotDevicePrincipal


class AlipayCommerceIotMdeviceprodDeviceUnbindModel(object):

    def __init__(self):
        self._biz_tid = None
        self._device_sn = None
        self._identify_type = None
        self._principal = None
        self._supplier_id = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        if isinstance(value, list):
            self._principal = list()
            for i in value:
                if isinstance(i, IotDevicePrincipal):
                    self._principal.append(i)
                else:
                    self._principal.append(IotDevicePrincipal.from_alipay_dict(i))
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        if self.principal:
            if isinstance(self.principal, list):
                for i in range(0, len(self.principal)):
                    element = self.principal[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.principal[i] = element.to_alipay_dict()
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
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
        o = AlipayCommerceIotMdeviceprodDeviceUnbindModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        if 'principal' in d:
            o.principal = d['principal']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


