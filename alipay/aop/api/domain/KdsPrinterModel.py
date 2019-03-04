#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KdsPrinterModel(object):

    def __init__(self):
        self._device_id = None
        self._name = None
        self._printer_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KdsPrinterModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'name' in d:
            o.name = d['name']
        if 'printer_id' in d:
            o.printer_id = d['printer_id']
        return o


