#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItapDeviceInfo(object):

    def __init__(self):
        self._fw_version = None
        self._hw_version = None
        self._manufacturer = None
        self._model = None
        self._product_name = None

    @property
    def fw_version(self):
        return self._fw_version

    @fw_version.setter
    def fw_version(self, value):
        self._fw_version = value
    @property
    def hw_version(self):
        return self._hw_version

    @hw_version.setter
    def hw_version(self, value):
        self._hw_version = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fw_version:
            if hasattr(self.fw_version, 'to_alipay_dict'):
                params['fw_version'] = self.fw_version.to_alipay_dict()
            else:
                params['fw_version'] = self.fw_version
        if self.hw_version:
            if hasattr(self.hw_version, 'to_alipay_dict'):
                params['hw_version'] = self.hw_version.to_alipay_dict()
            else:
                params['hw_version'] = self.hw_version
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItapDeviceInfo()
        if 'fw_version' in d:
            o.fw_version = d['fw_version']
        if 'hw_version' in d:
            o.hw_version = d['hw_version']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'model' in d:
            o.model = d['model']
        if 'product_name' in d:
            o.product_name = d['product_name']
        return o


