#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrintModel(object):

    def __init__(self):
        self._device_id = None
        self._enable = None
        self._name = None
        self._printer_id = None
        self._printer_type = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def printer_id(self):
        return self._printer_id

    @printer_id.setter
    def printer_id(self, value):
        self._printer_id = value
    @property
    def printer_type(self):
        return self._printer_type

    @printer_type.setter
    def printer_type(self, value):
        self._printer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.printer_id:
            if hasattr(self.printer_id, 'to_alipay_dict'):
                params['printer_id'] = self.printer_id.to_alipay_dict()
            else:
                params['printer_id'] = self.printer_id
        if self.printer_type:
            if hasattr(self.printer_type, 'to_alipay_dict'):
                params['printer_type'] = self.printer_type.to_alipay_dict()
            else:
                params['printer_type'] = self.printer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrintModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'enable' in d:
            o.enable = d['enable']
        if 'name' in d:
            o.name = d['name']
        if 'printer_id' in d:
            o.printer_id = d['printer_id']
        if 'printer_type' in d:
            o.printer_type = d['printer_type']
        return o


