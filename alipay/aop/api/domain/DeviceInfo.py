#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceInfo(object):

    def __init__(self):
        self._device_id = None
        self._device_type = None
        self._dv_sn = None
        self._manufacturer = None
        self._product_model = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def dv_sn(self):
        return self._dv_sn

    @dv_sn.setter
    def dv_sn(self, value):
        self._dv_sn = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    @property
    def product_model(self):
        return self._product_model

    @product_model.setter
    def product_model(self, value):
        self._product_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.dv_sn:
            if hasattr(self.dv_sn, 'to_alipay_dict'):
                params['dv_sn'] = self.dv_sn.to_alipay_dict()
            else:
                params['dv_sn'] = self.dv_sn
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.product_model:
            if hasattr(self.product_model, 'to_alipay_dict'):
                params['product_model'] = self.product_model.to_alipay_dict()
            else:
                params['product_model'] = self.product_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceInfo()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'dv_sn' in d:
            o.dv_sn = d['dv_sn']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'product_model' in d:
            o.product_model = d['product_model']
        return o


